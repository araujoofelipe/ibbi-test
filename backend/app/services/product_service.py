from fastapi import UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.models import Product
from app.schemas.schemas import ProductCreate
from app.repositories.product_repository import ProductRepository
import aiofiles
import os

class ProductService:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session
        self.repo = ProductRepository(db_session)

    async def create(self, product_create: ProductCreate, image: UploadFile = None):
        image_url = None
        if image:
            image_url = await self.save_image(image)
        
        product = Product(
            name=product_create.name,
            description=product_create.description,
            price_brl=product_create.price_brl,
            price_usd=product_create.price_usd,
            stock_quantity=product_create.stock_quantity,
            category_id=product_create.category_id,
            image_url=image_url
        )
        return await self.repo.create(product)

    async def save_image(self, image: UploadFile) -> str:
        upload_dir = 'uploads/images'
        os.makedirs(upload_dir, exist_ok=True)
        file_path = os.path.join(upload_dir, image.filename)
        
        async with aiofiles.open(file_path, 'wb') as out_file:
            content = await image.read()
            await out_file.write(content)
        
        return file_path

    async def list(self, skip: int = 0, limit: int = 10):
        return await self.repo.list(skip, limit)
