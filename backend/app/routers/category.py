from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.models import models
from app.schemas import schemas
from app.database.postgres import get_db
from app.services.category_service import CategoryService

router = APIRouter()

@router.post("/", response_model=schemas.Category)
async def create(category: schemas.CategoryCreate, db: AsyncSession = Depends(get_db)):
    service = CategoryService(db)
    return await service.create(category.model_dump())

@router.get("/", response_model=List[schemas.Category])
async def list(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    service = CategoryService(db)
    return await service.list(skip, limit)