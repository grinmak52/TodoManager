from fastapi import APIRouter

from api.api_v1.tasks import router as tasks_router
from api.api_v1.categories import router as categories_router

router = APIRouter()
router.include_router(tasks_router)
router.include_router(categories_router)