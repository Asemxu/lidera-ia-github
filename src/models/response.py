from pydantic import BaseModel

class Response(BaseModel):
    statusCode: int
    headers: dict
    isBase64Encoded: bool
    body: dict