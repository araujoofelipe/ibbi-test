from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.schemas import Order, OrderCreate
from app.services.order_service import OrderService
from app.database.postgres import get_db

router = APIRouter()

@router.post("/", response_model=Order)
async def create_order(order_create: OrderCreate, db: AsyncSession = Depends(get_db)):
    order_service = OrderService(db)
    return await order_service.create(order_create)

@router.get("/", response_model=List[Order])
async def list_orders(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    order_service = OrderService(db)
    return await order_service.list(skip, limit)
