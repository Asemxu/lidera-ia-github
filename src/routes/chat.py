from fastapi import APIRouter , Request
from src.controllers.chat_controller import ChatController
from src.models.logger import logger
from src.config.config import global_config
from src.models.chat.chat_request import ChatRequest , ChatRequestMessage

router = APIRouter()

chat_controller = ChatController(logger,global_config)

@router.post("/chat-asistant")
async def chat(request: Request, chat_request: ChatRequest):
    logger.info("Consult api chat asistant")
    return await chat_controller.process_chat(request) 

@router.post("/chat-lidera")
async def chat(request: Request, chat_request: ChatRequestMessage):
    logger.info("Consult api chat bot lidera")
    return await chat_controller.process_chat(request)