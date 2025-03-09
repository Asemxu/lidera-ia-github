from pydantic import BaseModel , validator
from src.utils.constants.prompt import MIN_WORDS_STORY , MIN_WORDS_STORY_MESSAGE
class QuestionRequestMultiple(BaseModel):
    number_of_questions: int
    story: str
    type_service: str
    
    @validator('story')
    def check_story_length(cls, v):
        min_length = MIN_WORDS_STORY
        if len(v.split()) < min_length:
            raise ValueError(MIN_WORDS_STORY_MESSAGE)
        return v