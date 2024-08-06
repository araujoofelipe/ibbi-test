from sqlalchemy.ext.asyncio import AsyncSession
from app.models.models import Order
from app.schemas.schemas import OrderCreate
from app.repositories.order_repository import OrderRepository

class OrderService:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session
        self.repo = OrderRepository(db_session)

    async def create(self, order_create: OrderCreate):
        order = Order(
            product_id=order_create.product_id,
            quantity=order_create.quantity,
            price_in_real=order_create.price_in_real,
            price_in_dollar=order_create.price_in_dollar
        )
        return await self.repo.create(order)

    async def list(self, skip: int = 0, limit: int = 10):
        return await self.repo.list(skip, limit)
