from typing import Annotated
from fastapi import APIRouter, status, Depends, HTTPException

from api.dependencies import get_task_service
from schemas.task import TaskRead, TaskCreate, TaskUpdate
from services.task import TaskService, TaskNotFoundError

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("")
async def get_task(service: Annotated[TaskService, Depends(get_task_service)]) -> list[TaskRead]:
    return await service.list_tasks()


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_task(
        payload: TaskCreate,
        service: Annotated[TaskService, Depends(get_task_service)],
) -> TaskRead:
    return await service.create_task(payload)


@router.patch("/{task_id}")
async def update_task(
        task_id: str,
        payload: TaskUpdate,
        service: Annotated[TaskService, Depends(get_task_service)],
) -> TaskRead:
    try:
        return await service.update_task(task_id, payload)
    except TaskNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
        task_id: str,
        service: Annotated[TaskService, Depends(get_task_service)],
) -> None:
    try:
        await service.delete_task(task_id)
    except TaskNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
