from fastapi import APIRouter
from src.controllers.env_controller import EnvController

router = APIRouter()
env_controller = EnvController()

@router.get("/env")
async def get_env():
    return await env_controller.get_env() 