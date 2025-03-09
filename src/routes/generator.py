from fastapi import APIRouter , Request
from src.controllers.question_controller import QuestionController
from src.utils.constants.questions import QUESTIONS
from src.models.logger import logger
from src.models.questions.questions_request import QuestionRequestMultiple

router = APIRouter()
question_controller = QuestionController(logger)

@router.post("/question-multiple")
async def chat(request: Request, questions_request_multiple: QuestionRequestMultiple):
    logger.info("Consult api generate questions multiple times")
    return await question_controller.generate_questions(request,QUESTIONS['MULTIPLE_CHOICE']) 