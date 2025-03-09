from abc import ABC, abstractmethod
from fastapi import Request

class Chat(ABC):
    @abstractmethod
    async def process(self, request: Request):
        pass