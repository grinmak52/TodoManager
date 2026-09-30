from fastapi import APIRouter

from api.api_v1.task import router as tasks_router

router = APIRouter()
router.include_router(tasks_router)