import '../models/model.dart';
import '../utils/api_constants.dart';
import 'api_service.dart';

class ModelService {
  final ApiService _apiService;

  ModelService(this._apiService);

  // 获取所有分类
  Future<List<Category>> getCategories() async {
    try {
      final response = await _apiService.get(ApiConstants.categories);
      return (response.data as List)
          .map((json) => Category.fromJson(json))
          .toList();
    } catch (e) {
      throw Exception('获取分类失败: $e');
    }
  }

  // 获取指定分类下的模型列表
  Future<List<MathModel>> getModelsByCategory(int categoryId) async {
    try {
      final response = await _apiService.get(
        ApiConstants.categoryModels(categoryId),
      );
      return (response.data as List)
          .map((json) => MathModel.fromJson(json))
          .toList();
    } catch (e) {
      throw Exception('获取模型列表失败: $e');
    }
  }

  // 获取模型详情
  Future<MathModel> getModelDetail(int modelId) async {
    try {
      final response = await _apiService.get(
        ApiConstants.modelDetail(modelId),
      );
      return MathModel.fromJson(response.data);
    } catch (e) {
      throw Exception('获取模型详情失败: $e');
    }
  }

  // 更新学习进度
  Future<LearningProgress> updateProgress(
    int modelId,
    int progressPercentage,
    bool isCompleted,
  ) async {
    try {
      final response = await _apiService.post(
        ApiConstants.progress,
        data: {
          'model_id': modelId,
          'progress_percentage': progressPercentage,
          'is_completed': isCompleted,
        },
      );
      return LearningProgress.fromJson(response.data);
    } catch (e) {
      throw Exception('更新进度失败: $e');
    }
  }

  // 获取我的学习进度
  Future<List<LearningProgress>> getMyProgress() async {
    try {
      final response = await _apiService.get(ApiConstants.myProgress);
      return (response.data as List)
          .map((json) => LearningProgress.fromJson(json))
          .toList();
    } catch (e) {
      throw Exception('获取学习进度失败: $e');
    }
  }

  // 添加收藏
  Future<void> addFavorite(int modelId) async {
    try {
      await _apiService.post(ApiConstants.addFavorite(modelId));
    } catch (e) {
      throw Exception('添加收藏失败: $e');
    }
  }

  // 取消收藏
  Future<void> removeFavorite(int modelId) async {
    try {
      await _apiService.delete(ApiConstants.removeFavorite(modelId));
    } catch (e) {
      throw Exception('取消收藏失败: $e');
    }
  }
}
