from pydantic import BaseModel
from typing import List

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    data_source: str
    messages: List[Message]

class ChatRequestMessage(BaseModel):
    messages: List[Message]
    