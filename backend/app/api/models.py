from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List

from app.core.database import get_db
from app.models.models import Category, Model, LearningProgress, Favorite, User
from app.schemas.model import (
    CategoryResponse,
    ModelResponse,
    ModelListResponse,
    LearningProgressBase,
    LearningProgressResponse
)
from app.api.auth import get_current_user

router = APIRouter(prefix="/models", tags=["模型"])


@router.get("/categories", response_model=List[CategoryResponse])
async def get_categories(db: AsyncSession = Depends(get_db)):
    """获取所有分类"""
    result = await db.execute(
        select(Category).order_by(Category.display_order, Category.id)
    )
    categories = result.scalars().all()
    return categories


@router.get("/categories/{category_id}/models", response_model=List[ModelListResponse])
async def get_models_by_category(
    category_id: int,
    db: AsyncSession = Depends(get_db)
):
    """根据分类ID获取模型列表"""
    result = await db.execute(
        select(Model)
        .where(Model.category_id == category_id)
        .order_by(Model.display_order, Model.id)
    )
    models = result.scalars().all()
    return models


@router.get("/{model_id}", response_model=ModelResponse)
async def get_model_detail(
    model_id: int,
    db: AsyncSession = Depends(get_db)
):
    """获取模型详情"""
    result = await db.execute(select(Model).where(Model.id == model_id))
    model = result.scalar_one_or_none()

    if not model:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="模型不存在"
        )

    return model


@router.post("/progress", response_model=LearningProgressResponse)
async def update_learning_progress(
    progress_data: LearningProgressBase,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """更新学习进度"""
    # 检查模型是否存在
    result = await db.execute(select(Model).where(Model.id == progress_data.model_id))
    model = result.scalar_one_or_none()
    if not model:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="模型不存在"
        )

    # 查找现有进度记录
    result = await db.execute(
        select(LearningProgress).where(
            LearningProgress.user_id == current_user.id,
            LearningProgress.model_id == progress_data.model_id
        )
    )
    existing_progress = result.scalar_one_or_none()

    if existing_progress:
        # 更新现有记录
        existing_progress.progress_percentage = progress_data.progress_percentage
        existing_progress.is_completed = progress_data.is_completed
        await db.commit()
        await db.refresh(existing_progress)
        return existing_progress
    else:
        # 创建新记录
        new_progress = LearningProgress(
            user_id=current_user.id,
            model_id=progress_data.model_id,
            progress_percentage=progress_data.progress_percentage,
            is_completed=progress_data.is_completed
        )
        db.add(new_progress)
        await db.commit()
        await db.refresh(new_progress)
        return new_progress


@router.get("/progress/my", response_model=List[LearningProgressResponse])
async def get_my_progress(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """获取我的学习进度"""
    result = await db.execute(
        select(LearningProgress)
        .where(LearningProgress.user_id == current_user.id)
        .order_by(LearningProgress.last_studied_at.desc())
    )
    progress_list = result.scalars().all()
    return progress_list


@router.post("/favorites/{model_id}", status_code=status.HTTP_201_CREATED)
async def add_favorite(
    model_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """添加收藏"""
    # 检查模型是否存在
    result = await db.execute(select(Model).where(Model.id == model_id))
    if not result.scalar_one_or_none():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="模型不存在"
        )

    # 检查是否已收藏
    result = await db.execute(
        select(Favorite).where(
            Favorite.user_id == current_user.id,
            Favorite.model_id == model_id
        )
    )
    if result.scalar_one_or_none():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="已收藏该模型"
        )

    # 创建收藏记录
    new_favorite = Favorite(user_id=current_user.id, model_id=model_id)
    db.add(new_favorite)
    await db.commit()

    return {"message": "收藏成功"}


@router.delete("/favorites/{model_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_favorite(
    model_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """取消收藏"""
    result = await db.execute(
        select(Favorite).where(
            Favorite.user_id == current_user.id,
            Favorite.model_id == model_id
        )
    )
    favorite = result.scalar_one_or_none()

    if not favorite:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="收藏记录不存在"
        )

    await db.delete(favorite)
    await db.commit()
