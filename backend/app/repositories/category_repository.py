# app/repositories/category_repository.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app import models

class CategoryRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, category_data):
        db_category = models.Category(**category_data)
        self.db.add(db_category)
        await self.db.commit()
        await self.db.refresh(db_category)
        return db_category

    async def list(self, skip: int = 0, limit: int = 10):
        result = await self.db.execute(select(models.Category).offset(skip).limit(limit))
        return result.scalars().all()
