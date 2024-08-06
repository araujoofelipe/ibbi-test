from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from app.database.postgres import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(15), index=True)
    description = Column(String, index=True)
    price_brl = Column(Float, nullable=False)
    price_usd = Column(Float, nullable=False)
    stock_quantity = Column(Integer, default=0)
    category_id = Column(Integer, ForeignKey('categories.id'))
    image_url = Column(String, nullable=True)

    category = relationship("Category", back_populates="products")
    orders = relationship("Order", back_populates="product")

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(15), index=True)
    description = Column(String, nullable=True)

    products = relationship("Product", back_populates="category")

class DollarPrice(Base):
    __tablename__ = 'dollar_prices'

    id = Column(Integer, primary_key=True, index=True)
    price = Column(Float, nullable=False)
    updated_at = Column(DateTime, nullable=False)

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    price_in_real = Column(Float, nullable=False)
    price_in_dollar = Column(Float, nullable=False)

    product = relationship("Product", back_populates="orders")
