from sqlalchemy import select
from app.repositories.product_repository import ProductRepository
from app.models.models import Product

class ProductService:
    def __init__(self, db):
        self.repo = ProductRepository(db)

    async def create(self, product_data):
        return await self.repo.create(product_data)

    async def list(self, skip: int = 0, limit: int = 10):
        return await self.repo.list(skip, limit)
    
    async def update_product_dollar_prices(self, dollar_price: float):
        async with self.db_session() as session:
            async with session.begin():
                products = await session.execute(select(Product))
                products = products.scalars().all()

                for product in products:
                    product.price_in_dollar = product.price_in_real / dollar_price

                await session.commit()
