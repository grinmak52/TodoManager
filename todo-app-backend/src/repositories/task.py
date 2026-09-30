from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from orm import Task


class TaskRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self) -> list[Task]:
        result = await self.session.scalars(select(Task))
        return list(result)

    async def get_by_id(self, task_id: str) -> Task | None:
        return await self.session.get(Task, task_id)

    async def create(self, title: str) -> Task:
        new_task = Task(title=title, completed=False)
        self.session.add(new_task)
        return new_task

    async def delete(self, task: Task) -> None:
        await self.session.delete(task)