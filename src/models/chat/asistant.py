from fastapi import Request
from src.api.chat import get_chat_engine 
from src.utils.helpers.response import build_response, build_error_response , handle_exception
import asyncio
from src.utils.helpers.body import get_json_body 
from src.utils.helpers.error import InvalidDataSourceError
from src.interfaces.chat import Chat
from src.utils.constants.content import FORMAT_TEXT
from src.utils.constants.messages import  MESSAGES_REQUIRED, LAST_MESSAGE_CONTENT_REQUIRED
from src.utils.constants.status_code import ERROR
from functools import lru_cache

class Asistant(Chat):
    def __init__(self, logger, config):
        self.logger = logger
        self.config = config

    async def process(self, request: Request):
        try:
            loop = asyncio.get_event_loop()
            json_body = await get_json_body(request,self.logger)
            thread_id = request.headers.get("Chat-Thread-id")
            chat_engine = await self.initialize_chat_engine(json_body, thread_id)
            response = await loop.run_in_executor(None,self.handle_chat,chat_engine, json_body)
            return build_response(response,FORMAT_TEXT)
        except ValueError as e:
            return build_error_response(ERROR, str(e))
        except InvalidDataSourceError as e:
            return build_error_response(ERROR, str(e))
        except Exception as e:
            return handle_exception(e,self.logger)

    async def initialize_chat_engine(self, json_body, thread_id):
        data_source = json_body.get("data_source")
        chat_engine = await get_chat_engine(data_source, thread_id, self.config)
        if not chat_engine:
            raise InvalidDataSourceError(data_source)
        return chat_engine

    @lru_cache(maxsize=10000)
    def handle_chat(self, chat_engine, json_body):
        messages = json_body.get("messages", [])
        if not messages:
            raise ValueError(MESSAGES_REQUIRED)
        last_message = messages[-1].get("content")
        if not last_message:
            raise ValueError(LAST_MESSAGE_CONTENT_REQUIRED)
        return chat_engine.chat(last_message)

    

