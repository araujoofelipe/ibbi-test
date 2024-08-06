from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app import models

class DollarPriceRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get(self):
        result = await self.db.execute(select(models.DollarPrice))
        return result.scalars().first()

    async def create_or_update(self, price: float):
        db_price = await self.get()
        if db_price is None:
            db_price = models.DollarPrice(price=price)
            self.db.add(db_price)
        else:
            db_price.price = price
        await self.db.commit()
        await self.db.refresh(db_price)
        return db_price
