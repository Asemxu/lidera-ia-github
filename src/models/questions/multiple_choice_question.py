from fastapi import Request
from src.interfaces.question import Question
from src.utils.constants.status_code import ERROR
from src.utils.helpers.body import get_json_body 
from src.api.questions import get_multiple_questions
from src.utils.constants.content import FORMAT_JSON
from src.utils.constants.questions import MAX_INTENTS , INITIAL_INTENTS
from src.utils.helpers.response import build_response , build_error_response , handle_exception
from src.utils.helpers.validate_format import validate_format
from src.utils.constants.patterns_question import multiple_choice_question_pattern
# from src.utils.helpers.process_text import process_text
import asyncio


class MultipleChoiceQuestion(Question):
    def __init__(self, logger):
        self.logger = logger
    
    async def generate(self, request: Request):
        try:
            loop = asyncio.get_event_loop()
            json_body = await get_json_body(request,self.logger)
            story = json_body['story']
            num_of_questions = json_body['number_of_questions']
            story = story.replace("\n", "").replace("\r", "")
            # story = process_text(story)
            isValidQuestions = False
            questions ={}
            intents = INITIAL_INTENTS
            while isValidQuestions == False and intents < MAX_INTENTS:
                questions = await loop.run_in_executor(None,get_multiple_questions, num_of_questions , story)
                if(validate_format(questions['text'],multiple_choice_question_pattern)):
                    questions['status'] = "Valid format"
                    isValidQuestions = True
                    print("Valid format")
                else:
                    questions['status'] = "Invalid format"
                    intents += 1
                    if intents == 5:
                        questions['status'] = "Bad format story"
                    print("Invalid format")
            
            return build_response(questions,FORMAT_JSON)
        except ValueError as e:
            return build_error_response(ERROR, str(e))
        except Exception as e:
            return handle_exception(e,self.logger)
