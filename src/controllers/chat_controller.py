from fastapi import  Request
from src.services.chat_service import ChatService
from src.models.chat.chat_request import ChatRequest

class ChatController:
    def __init__(self, logger , config):
        self.logger = logger
        self.config = config
        self.chat_service = ChatService(config, logger)
        
    async def process_chat(self,request:Request):
       response = await self.chat_service.process_chat(request)
       return response