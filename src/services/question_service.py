from src.models.questions.question_processor import QuestionProcessor
class QuestionService:
    def __init__(self, logger):
        self.logger = logger
        self.question_processor = QuestionProcessor(self.logger)

    async def process_questions(self,request,type_question):
        return await self.question_processor.process_questions(request,type_question)