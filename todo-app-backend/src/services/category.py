from sqlalchemy.ext.asyncio import AsyncSession

from repositories.category import CategoryRepository
from schemas.category import CategoryRead, CategoryCreate, CategoryUpdate


class CategoryNotFoundError(Exception):
    pass


class CategoryService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.repository = CategoryRepository(session)

    async def list_categories(self) -> list[CategoryRead]:
        categories = await self.repository.get_all()
        return [CategoryRead.model_validate(category) for category in categories]

    async def create_category(self, payload: CategoryCreate) -> CategoryRead:
        category = await self.repository.create(name=payload.name)
        await self.session.commit()
        await self.session.refresh(category)
        return CategoryRead.model_validate(category)

    async def update_category(self, category_id: str, payload: CategoryUpdate) -> CategoryRead:
        category = await self.repository.get_by_id(category_id)
        if category is None:
            raise CategoryNotFoundError
        if payload.name is not None:
            category.name = payload.name
        await self.session.commit()
        await self.session.refresh(category)
        return CategoryRead.model_validate(category)

    async def delete_category(self, category_id: str) -> None:
        category = await self.repository.get_by_id(category_id)
        if category is None:
            raise CategoryNotFoundError
        await self.repository.delete(category)
        await self.session.commit()