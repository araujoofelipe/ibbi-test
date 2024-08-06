from datetime import datetime
from pydantic import BaseModel, HttpUrl, constr
from typing import Optional

class CategoryBase(BaseModel):
    name: constr(max_length=15)
    description: Optional[str] = None

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True

class ProductBase(BaseModel):
    name: constr(max_length=15)
    description: str
    price_brl: float
    price_usd: float
    stock_quantity: int
    category_id: int
    image_url: Optional[HttpUrl] = None

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    category: Category

    class Config:
        orm_mode = True

class DollarPriceCreate(ProductBase):
    pass
        
class DollarPrice(BaseModel):
    id: int
    price: float
    updated_at: datetime

    class Config:
        orm_mode = True