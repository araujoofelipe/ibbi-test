from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.models import Order

class OrderRepository:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create(self, order: Order):
        async with self.db_session() as session:
            session.add(order)
            await session.commit()
            await session.refresh(order)
            return order

    async def list(self, skip: int = 0, limit: int = 10):
        async with self.db_session() as session:
            stmt = select(Order).offset(skip).limit(limit)
            result = await session.execute(stmt)
            return result.scalars().all()
