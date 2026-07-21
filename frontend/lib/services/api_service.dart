import 'package:dio/dio.dart';
import 'package:shared_preferences/shared_preferences.dart';
import '../utils/api_constants.dart';

class ApiService {
  late Dio _dio;
  String? _token;

  ApiService() {
    _dio = Dio(BaseOptions(
      baseUrl: ApiConstants.baseUrl,
      connectTimeout: const Duration(seconds: 10),
      receiveTimeout: const Duration(seconds: 10),
      headers: {
        'Content-Type': 'application/json',
      },
    ));

    // 添加拦截器
    _dio.interceptors.add(InterceptorsWrapper(
      onRequest: (options, handler) async {
        // 添加token到请求头
        if (_token != null) {
          options.headers['Authorization'] = 'Bearer $_token';
        }
        return handler.next(options);
      },
      onError: (error, handler) {
        // 统一错误处理
        return handler.next(error);
      },
    ));
  }

  // 设置Token
  Future<void> setToken(String token) async {
    _token = token;
    final prefs = await SharedPreferences.getInstance();
    await prefs.setString('auth_token', token);
  }

  // 获取Token
  Future<String?> getToken() async {
    if (_token != null) return _token;
    final prefs = await SharedPreferences.getInstance();
    _token = prefs.getString('auth_token');
    return _token;
  }

  // 清除Token
  Future<void> clearToken() async {
    _token = null;
    final prefs = await SharedPreferences.getInstance();
    await prefs.remove('auth_token');
  }

  // 通用GET请求
  Future<Response> get(String path, {Map<String, dynamic>? queryParameters}) async {
    await getToken();
    return await _dio.get(path, queryParameters: queryParameters);
  }

  // 通用POST请求
  Future<Response> post(String path, {dynamic data}) async {
    await getToken();
    return await _dio.post(path, data: data);
  }

  // 通用PUT请求
  Future<Response> put(String path, {dynamic data}) async {
    await getToken();
    return await _dio.put(path, data: data);
  }

  // 通用DELETE请求
  Future<Response> delete(String path) async {
    await getToken();
    return await _dio.delete(path);
  }
}
