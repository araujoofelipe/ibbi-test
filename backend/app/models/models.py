from sqlalchemy import Column, DateTime, Integer, String, Text, ForeignKey, Float, func
from sqlalchemy.orm import relationship
from app.database.postgres import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(15), unique=True, nullable=False)
    description = Column(Text, nullable=True)

    products = relationship("Product", back_populates="category")

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(15), nullable=False)
    description = Column(Text, nullable=False)
    price_brl = Column(Float, nullable=False)
    price_usd = Column(Float, nullable=False)
    stock_quantity = Column(Integer, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"))
    image_url = Column(String, nullable=True)

    category = relationship("Category", back_populates="products")

class DollarPrice(Base):
    __tablename__ = "dollar_price"

    id = Column(Integer, primary_key=True, index=True)
    price = Column(Float, nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    __table_args__ = {'extend_existing': True}