import asyncio
from fastapi import FastAPI
from app.database.postgres import engine, Base
from app.routers import category, product, dollar_price, order
from app.cron.update_dollar import update_dollar

async def lifespan(app: FastAPI):
    # Configura o banco de dados
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    # Define a tarefa de atualização periódica
    task = asyncio.create_task(update_dollar())
    
    yield
    
    # Aguarda a tarefa de atualização periódica terminar (se necessário)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        pass

app = FastAPI(lifespan=lifespan)

app.include_router(category.router, prefix="/categories", tags=["categories"])
app.include_router(product.router, prefix="/products", tags=["products"])
app.include_router(dollar_price.router, prefix="/dollar-price", tags=["dollar-price"])
app.include_router(order.router, prefix="/orders", tags=["orders"])
