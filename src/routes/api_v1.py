from fastapi import APIRouter
from src.routes.chat import router as chat_router
from src.routes.generator import router as generator_router
from src.routes.env import router as env_router


router = APIRouter()

router.include_router(chat_router, tags=["chat"])
router.include_router(generator_router, tags=["generator"])
router.include_router(env_router, tags=["env"])


def setup_routes(app):
    app.include_router(router, prefix="/api/v1")