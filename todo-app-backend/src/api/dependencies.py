from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from orm import db_helper
from services.category import CategoryService
from services.task import TaskService


async def get_task_service(
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
) -> TaskService:
    return TaskService(session)


async def get_category_service(
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
) -> CategoryService:
    return CategoryService(session)
