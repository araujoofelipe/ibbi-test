from app.repositories.category_repository import CategoryRepository

class CategoryService:
    def __init__(self, db):
        self.repo = CategoryRepository(db)

    async def create(self, category_data):
        return await self.repo.create(category_data)

    async def list(self, skip: int = 0, limit: int = 10):
        return await self.repo.list(skip, limit)
