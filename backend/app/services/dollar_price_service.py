import os
from dotenv import load_dotenv
from sqlalchemy import select
from app.repositories.dollar_price_repository import DollarPriceRepository
from app.helpers.api_client import ApiClient
from app.models.models import DollarPrice

# Carregar variáveis de ambiente do .env
load_dotenv()

class DollarPriceService:
    def __init__(self, db, api_client: ApiClient):
        self.repo = DollarPriceRepository(db)
        self.api_client = api_client
        self.default_url = os.getenv("DOLLAR_API_ENDPOINT")

    async def get_price(self):
        return await self.repo.get()

    async def update_price(self):
        async with self.db_session() as session:
            # Obtém o preço do dólar da API externa
            dollar_price = await self.fetch_dollar_price()

            # Atualiza o registro do preço do dólar no banco de dados
            async with session.begin():
                existing_record = await session.execute(select(DollarPrice))
                existing_record = existing_record.scalar_one_or_none()

                if existing_record:
                    existing_record.price = dollar_price
                else:
                    new_record = DollarPrice(price=dollar_price)
                    session.add(new_record)
                await session.commit()

            return dollar_price
