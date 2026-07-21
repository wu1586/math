from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Text, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base
import enum


class User(Base):
    """用户表"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # 关系
    learning_progress = relationship("LearningProgress", back_populates="user")
    favorites = relationship("Favorite", back_populates="user")


class CategoryEnum(str, enum.Enum):
    """模型分类枚举"""
    MATHEMATICAL_PROGRAMMING = "mathematical_programming"  # 数学规划
    EVALUATION_DECISION = "evaluation_decision"  # 综合评价与决策
    PREDICTION = "prediction"  # 预测类模型
    STATISTICS = "statistics"  # 概率统计与数据分析
    DIFFERENTIAL_EQUATIONS = "differential_equations"  # 微分方程与系统动力学
    GRAPH_THEORY = "graph_theory"  # 图论与网络优化
    INTELLIGENT_OPTIMIZATION = "intelligent_optimization"  # 智能优化算法
    MACHINE_LEARNING = "machine_learning"  # 机器学习与数据挖掘
    OPERATIONS_RESEARCH = "operations_research"  # 运筹学经典模型
    OTHER_MODELS = "other_models"  # 其他专项模型


class Category(Base):
    """模型分类表"""
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    name_en = Column(Enum(CategoryEnum), unique=True, nullable=False)
    description = Column(Text)
    icon = Column(String(50))  # 图标名称
    display_order = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # 关系
    models = relationship("Model", back_populates="category")


class Model(Base):
    """数学模型表"""
    __tablename__ = "models"

    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    name = Column(String(100), nullable=False)
    name_en = Column(String(100))
    description = Column(Text)
    theory_content = Column(Text)  # 理论知识
    case_content = Column(Text)  # 案例分析
    code_content = Column(Text)  # 代码示例
    demo_url = Column(String(255))  # 交互Demo链接
    difficulty_level = Column(Integer, default=1)  # 难度等级 1-5
    display_order = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # 关系
    category = relationship("Category", back_populates="models")
    learning_progress = relationship("LearningProgress", back_populates="model")
    favorites = relationship("Favorite", back_populates="model")


class LearningProgress(Base):
    """学习进度表"""
    __tablename__ = "learning_progress"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    model_id = Column(Integer, ForeignKey("models.id"), nullable=False)
    is_completed = Column(Boolean, default=False)
    progress_percentage = Column(Integer, default=0)  # 进度百分比 0-100
    last_studied_at = Column(DateTime(timezone=True), server_default=func.now())
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # 关系
    user = relationship("User", back_populates="learning_progress")
    model = relationship("Model", back_populates="learning_progress")


class Favorite(Base):
    """收藏表"""
    __tablename__ = "favorites"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    model_id = Column(Integer, ForeignKey("models.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # 关系
    user = relationship("User", back_populates="favorites")
    model = relationship("Model", back_populates="favorites")
