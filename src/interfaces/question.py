from abc import ABC, abstractmethod
from fastapi import Request

class Question(ABC):
    @abstractmethod
    async def generate(self, request: Request):
        pass