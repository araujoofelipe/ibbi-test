from datetime import datetime
from pydantic import BaseModel, HttpUrl, constr
from typing import Optional

# Category Schemas
class CategoryBase(BaseModel):
    name: constr(max_length=15)
    description: Optional[str] = None

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True

# Product Schemas
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

# DollarPrice Schemas
class DollarPriceBase(BaseModel):
    price: float
    updated_at: datetime

class DollarPriceCreate(BaseModel):
    price: float

class DollarPrice(DollarPriceBase):
    id: int

    class Config:
        orm_mode = True

# Order Schemas
class OrderBase(BaseModel):
    product_id: int
    quantity: int
    price_in_real: float
    price_in_dollar: float

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int

    class Config:
        orm_mode = True
