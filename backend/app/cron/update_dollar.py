import asyncio
from app.services.dollar_price_service import DollarPriceService
from app.services.product_service import ProductService
from app.helpers.api_client import ApiClient
from app.database.postgres import AsyncSession, engine


async def update_dollar():
    async with engine.begin() as conn:
        async_session = AsyncSession(conn)
        dollar_service = DollarPriceService(async_session, ApiClient())
        product_service = ProductService(async_session)

        # Atualiza o preço do dólar
        dollar_price = await dollar_service.update_price()

        # Atualiza o preço em dólar para todos os produtos
        await product_service.update_product_dollar_prices(dollar_price)

        while True:
            # Atualiza o preço do dólar a cada 10 minutos
            await asyncio.sleep(1.0)
            dollar_price = await dollar_service.update_price()
            await product_service.update_product_dollar_prices(dollar_price)
