from fastapi import APIRouter, Body, Depends, Query, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional
from app.schemas import schemas
from app.database.postgres import get_db
from app.services.dollar_price_service import DollarPriceService
from app.helpers.api_client import ApiClient
import os

router = APIRouter()
api_client = ApiClient()

@router.get("/", response_model=schemas.DollarPrice)
async def get_price(db: AsyncSession = Depends(get_db)):
    service = DollarPriceService(db, api_client)
    price = await service.get_price()
    if price is None:
        raise HTTPException(status_code=404, detail="Price not found")
    return price

@router.post("/", response_model=schemas.DollarPrice)
async def update_price(
    url: Optional[str] = Query(None),  
    params: Optional[dict] = Body(None),
    db: AsyncSession = Depends(get_db)
):
    if url is None:
        url = os.getenv("DOLLAR_API_ENDPOINT")
    service = DollarPriceService(db, api_client)
    try:
        return await service.update_price(url, params)
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))
