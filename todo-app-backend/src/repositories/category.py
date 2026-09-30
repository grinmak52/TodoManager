from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from orm.models import Category


class CategoryRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self) -> list[Category]:
        result = await self.session.scalars(select(Category))
        return list(result)

    async def get_by_id(self, category_id: str) -> Category | None:
        return await self.session.get(Category, category_id)

    async def create(self, name: str) -> Category:
        category = Category(name=name)
        self.session.add(category)
        return category

    async def delete(self, category: Category) -> None:
        await self.session.delete(category)