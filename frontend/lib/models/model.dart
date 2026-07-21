class Category {
  final int id;
  final String name;
  final String nameEn;
  final String? description;
  final String? icon;
  final int displayOrder;
  final DateTime createdAt;

  Category({
    required this.id,
    required this.name,
    required this.nameEn,
    this.description,
    this.icon,
    required this.displayOrder,
    required this.createdAt,
  });

  factory Category.fromJson(Map<String, dynamic> json) {
    return Category(
      id: json['id'],
      name: json['name'],
      nameEn: json['name_en'],
      description: json['description'],
      icon: json['icon'],
      displayOrder: json['display_order'],
      createdAt: DateTime.parse(json['created_at']),
    );
  }
}

class MathModel {
  final int id;
  final int categoryId;
  final String name;
  final String? nameEn;
  final String? description;
  final String? theoryContent;
  final String? caseContent;
  final String? codeContent;
  final String? demoUrl;
  final int difficultyLevel;
  final int displayOrder;
  final DateTime createdAt;
  final DateTime? updatedAt;

  MathModel({
    required this.id,
    required this.categoryId,
    required this.name,
    this.nameEn,
    this.description,
    this.theoryContent,
    this.caseContent,
    this.codeContent,
    this.demoUrl,
    required this.difficultyLevel,
    required this.displayOrder,
    required this.createdAt,
    this.updatedAt,
  });

  factory MathModel.fromJson(Map<String, dynamic> json) {
    return MathModel(
      id: json['id'],
      categoryId: json['category_id'],
      name: json['name'],
      nameEn: json['name_en'],
      description: json['description'],
      theoryContent: json['theory_content'],
      caseContent: json['case_content'],
      codeContent: json['code_content'],
      demoUrl: json['demo_url'],
      difficultyLevel: json['difficulty_level'],
      displayOrder: json['display_order'],
      createdAt: DateTime.parse(json['created_at']),
      updatedAt: json['updated_at'] != null ? DateTime.parse(json['updated_at']) : null,
    );
  }
}

class LearningProgress {
  final int id;
  final int userId;
  final int modelId;
  final bool isCompleted;
  final int progressPercentage;
  final DateTime lastStudiedAt;
  final DateTime createdAt;

  LearningProgress({
    required this.id,
    required this.userId,
    required this.modelId,
    required this.isCompleted,
    required this.progressPercentage,
    required this.lastStudiedAt,
    required this.createdAt,
  });

  factory LearningProgress.fromJson(Map<String, dynamic> json) {
    return LearningProgress(
      id: json['id'],
      userId: json['user_id'],
      modelId: json['model_id'],
      isCompleted: json['is_completed'],
      progressPercentage: json['progress_percentage'],
      lastStudiedAt: DateTime.parse(json['last_studied_at']),
      createdAt: DateTime.parse(json['created_at']),
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'model_id': modelId,
      'is_completed': isCompleted,
      'progress_percentage': progressPercentage,
    };
  }
}
