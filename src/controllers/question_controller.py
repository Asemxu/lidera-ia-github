from fastapi import  Request
from src.services.question_service import QuestionService

class QuestionController:
    def __init__(self, logger):
        self.logger = logger
        self.question_service = QuestionService(logger)
        
    async def generate_questions(self,request: Request, type_question):
       return await self.question_service.process_questions(request,type_question)