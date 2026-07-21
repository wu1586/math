from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class CategoryBase(BaseModel):
    """分类基础模式"""
    name: str
    name_en: str
    description: Optional[str] = None
    icon: Optional[str] = None
    display_order: int = 0


class CategoryResponse(CategoryBase):
    """分类响应模式"""
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class ModelBase(BaseModel):
    """模型基础模式"""
    name: str
    name_en: Optional[str] = None
    description: Optional[str] = None
    difficulty_level: int = 1
    display_order: int = 0


class ModelCreate(ModelBase):
    """模型创建模式"""
    category_id: int
    theory_content: Optional[str] = None
    case_content: Optional[str] = None
    code_content: Optional[str] = None
    demo_url: Optional[str] = None


class ModelResponse(ModelBase):
    """模型响应模式"""
    id: int
    category_id: int
    theory_content: Optional[str] = None
    case_content: Optional[str] = None
    code_content: Optional[str] = None
    demo_url: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class ModelListResponse(BaseModel):
    """模型列表响应"""
    id: int
    name: str
    description: Optional[str] = None
    difficulty_level: int
    category_id: int

    class Config:
        from_attributes = True


class LearningProgressBase(BaseModel):
    """学习进度基础模式"""
    model_id: int
    progress_percentage: int = 0
    is_completed: bool = False


class LearningProgressResponse(LearningProgressBase):
    """学习进度响应模式"""
    id: int
    user_id: int
    last_studied_at: datetime
    created_at: datetime

    class Config:
        from_attributes = True


class FavoriteResponse(BaseModel):
    """收藏响应模式"""
    id: int
    user_id: int
    model_id: int
    created_at: datetime

    class Config:
        from_attributes = True
