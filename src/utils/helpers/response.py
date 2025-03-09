from src.config.environment import LLM_MODEL
from src.utils.constants.status_code import SUCCESS
from fastapi.responses import JSONResponse
from src.utils.constants.messages import  INTERNAL_SERVER_ERROR_MESSAGE
from src.utils.constants.status_code import INTERNAL_SERVER_ERROR
from src.utils.constants.content import FORMAT_JSON

def build_response(result,type):
    body = {
        "model": LLM_MODEL,
        "message": {"role": "assistant", "content":  result if type == FORMAT_JSON else str(result)},
    }
    return JSONResponse(content={"statusCode": SUCCESS, "body": body})

def build_error_response(status_code, message):
    return JSONResponse(content={"statusCode": status_code, "body": {"error": message}})


def handle_exception(e,logger):
    logger.error("An unexpected error occurred: %s", e, exc_info=True)
    return build_error_response(INTERNAL_SERVER_ERROR, INTERNAL_SERVER_ERROR_MESSAGE(e))
