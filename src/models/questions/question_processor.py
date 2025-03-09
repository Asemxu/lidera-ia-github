from src.models.questions.multiple_choice_question import MultipleChoiceQuestion 

class QuestionProcessor:
    def __init__(self,logger):
        self.logger = logger
        self.questionsHandlers = {
            "MULTIPLE_CHOICE": MultipleChoiceQuestion(self.logger),
        }
            
    async def process_questions(self, request, type_question):
        handler = self.questionsHandlers.get(type_question)
        result = await handler.generate(request)
        return result