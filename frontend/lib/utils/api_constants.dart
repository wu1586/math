class ApiConstants {
  // 基础URL - 根据实际情况修改
  static const String baseUrl = 'http://localhost:8000';

  // 认证相关
  static const String register = '/auth/register';
  static const String login = '/auth/login';
  static const String me = '/auth/me';

  // 模型相关
  static const String categories = '/models/categories';
  static String categoryModels(int categoryId) => '/models/categories/$categoryId/models';
  static String modelDetail(int modelId) => '/models/$modelId';

  // 学习进度
  static const String progress = '/models/progress';
  static const String myProgress = '/models/progress/my';

  // 收藏
  static String addFavorite(int modelId) => '/models/favorites/$modelId';
  static String removeFavorite(int modelId) => '/models/favorites/$modelId';
}
