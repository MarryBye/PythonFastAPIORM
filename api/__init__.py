from fastapi.routing import APIRouter
from api.v1 import router as v1_router

router = APIRouter()
router.include_router(v1_router, tags=["v1"])