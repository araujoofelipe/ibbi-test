# app/repositories/product_repository.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app import models
from app.models.models import Product

class ProductRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, product_data):
        db_product = models.Product(**product_data)
        self.db.add(db_product)
        await self.db.commit()
        await self.db.refresh(db_product)
        return db_product

    async def list(self, skip: int = 0, limit: int = 10):
         async with self.db_session() as session:
            stmt = select(Product).filter(Product.stock_quantity > 0).offset(skip).limit(limit)
            result = await session.execute(stmt)
            return result.scalars().all()
