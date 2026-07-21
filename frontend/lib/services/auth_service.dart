import '../models/user.dart';
import '../utils/api_constants.dart';
import 'api_service.dart';

class AuthService {
  final ApiService _apiService;

  AuthService(this._apiService);

  // 用户注册
  Future<User> register(String username, String email, String password) async {
    try {
      final response = await _apiService.post(
        ApiConstants.register,
        data: RegisterRequest(
          username: username,
          email: email,
          password: password,
        ).toJson(),
      );

      return User.fromJson(response.data);
    } catch (e) {
      throw Exception('注册失败: $e');
    }
  }

  // 用户登录
  Future<TokenResponse> login(String username, String password) async {
    try {
      final response = await _apiService.post(
        ApiConstants.login,
        data: LoginRequest(
          username: username,
          password: password,
        ).toJson(),
      );

      final tokenResponse = TokenResponse.fromJson(response.data);
      await _apiService.setToken(tokenResponse.accessToken);
      return tokenResponse;
    } catch (e) {
      throw Exception('登录失败: $e');
    }
  }

  // 获取当前用户信息
  Future<User> getCurrentUser() async {
    try {
      final response = await _apiService.get(ApiConstants.me);
      return User.fromJson(response.data);
    } catch (e) {
      throw Exception('获取用户信息失败: $e');
    }
  }

  // 登出
  Future<void> logout() async {
    await _apiService.clearToken();
  }

  // 检查是否已登录
  Future<bool> isLoggedIn() async {
    final token = await _apiService.getToken();
    return token != null && token.isNotEmpty;
  }
}
