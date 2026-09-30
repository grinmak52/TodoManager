from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from api.dependencies import get_category_service
from schemas.category import CategoryRead, CategoryCreate, CategoryUpdate
from services.category import CategoryService, CategoryNotFoundError


router = APIRouter(prefix="/categories", tags=["categories"])


@router.get("")
async def get_categories(
        service: Annotated[CategoryService, Depends(get_category_service)],
) -> list[CategoryRead]:
    return await service.list_categories()


@router.post("")
async def create_category(
        service: Annotated[CategoryService, Depends(get_category_service)],
        payload: CategoryCreate,
) -> CategoryRead:
    return await service.create_category(payload)


@router.patch("/{category_id}")
async def update_category(
        service: Annotated[CategoryService, Depends(get_category_service)],
        category_id: str,
        payload: CategoryUpdate,
) -> CategoryRead:
    try:
        return await service.update_category(category_id, payload)
    except CategoryNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found",
        )


@router.delete("/{category_id}")
async def delete_category(
        service: Annotated[CategoryService, Depends(get_category_service)],
        category_id: str,
) -> None:
    try:
        await service.delete_category(category_id)
    except CategoryNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found",
        )