from src.utils.constants.status_code import ERROR
from src.interfaces.chat import Chat
from fastapi import Request
from src.utils.constants.content import FORMAT_TEXT
from src.utils.helpers.response import build_response, build_error_response , handle_exception
from src.utils.helpers.body import get_json_body 
from src.api.chat import generate_embeddings , get_relevant_documents , get_chat_response

class Bot(Chat):
    def __init__(self, logger ):
        self.logger = logger
    
    async def process(self, request: Request):
        try:
            json_body = await get_json_body(request,self.logger)
            messages = json_body['messages']
            last_message = messages[-1]['content']
            query_embeddings = generate_embeddings(last_message)
            relevant_documents = get_relevant_documents(query_embeddings)
            tuple_messages = tuple(tuple(message.items()) for message in messages)
            tuple_relevant_documents = tuple(relevant_documents)
            tuple_relevant_documents = tuple(tuple(doc.items()) for doc in relevant_documents)
            llm_response = get_chat_response(tuple_messages, tuple_relevant_documents)
            return build_response(llm_response['message']['content'],FORMAT_TEXT)
        except ValueError as e:
            return build_error_response(ERROR, str(e))
        except Exception as e:
            return handle_exception(e,self.logger)
