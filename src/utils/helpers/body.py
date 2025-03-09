from src.utils.constants.messages import INVALID_JSON_BODY 
from fastapi import Request

def log_body(body,logger):
    logger.info("Sent Body Request: %s", body)
    logger.info("Body decoded: %s", body)
      
async def get_json_body(request: Request,logger):
    body = await request.json()
    log_body(body,logger)
    if not body:
        raise ValueError(INVALID_JSON_BODY)
    return body

