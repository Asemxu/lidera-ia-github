from src.models.chat.asistant import Asistant
from src.models.chat.bot import Bot

class ChatService:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.asistant = Asistant(logger,config)
        self.bot = Bot(logger)

    def isValidChatThread(self, request):
        thread_id = request.headers.get("Chat-Thread-id")
        if not thread_id:
            return False
        self.logger.info("Thread ID: %s", thread_id)
        return True
    
    async def process_chat(self,request):
        if(self.isValidChatThread(request)):
            return await self.asistant.process(request)
        else:
            return await self.bot.process(request)