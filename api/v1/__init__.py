from fastapi.routing import APIRouter
from api.v1.users import router as users_router
from api.v1.auth import router as auth_router

router = APIRouter(prefix="/v1")
router.include_router(users_router)
router.include_router(auth_router)