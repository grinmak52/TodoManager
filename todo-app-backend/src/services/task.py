from sqlalchemy.ext.asyncio import AsyncSession

from repositories.task import TaskRepository
from schemas.task import TaskRead, TaskUpdate, TaskCreate

class TaskNotFoundError(Exception):
    pass

class TaskService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.tasks_repository = TaskRepository(session)

    async def list_tasks(self) -> list[TaskRead]:
        tasks = await self.tasks_repository.get_all()
        return [TaskRead.model_validate(task) for task in tasks]

    async def create_task(self, payload: TaskCreate) -> TaskRead:
        task = await self.tasks_repository.create(title=payload.title)
        await self.session.commit()
        await self.session.refresh(task)
        return TaskRead.model_validate(task)

    async def update_task(self, task_id: str, payload: TaskUpdate) -> TaskRead:
        task = await self.tasks_repository.get_by_id(task_id)
        if task is None:
            raise TaskNotFoundError

        if payload.title is not None:
            task.title = payload.title
        if payload.completed is not None:
            task.completed = payload.completed

        await self.session.commit()
        await self.session.refresh(task)
        return TaskRead.model_validate(task)

    async def delete_task(self, task_id:str) -> None:
        task = await self.tasks_repository.get_by_id(task_id)
        if task is None:
            raise TaskNotFoundError

        await self.tasks_repository.delete(task)
        await self.session.commit()