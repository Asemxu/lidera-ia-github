import requests
from src.utils.constants.prompt import GETPROMPTMULTIPECHOICEQUESTION
from src.utils.constants.questions import MAX_TIMEOUT

from src.config.environment import LLM_HOST, LLM_MODEL
def get_multiple_questions(num_of_questions,story):
    text = GETPROMPTMULTIPECHOICEQUESTION(num_of_questions, story)
    data = {
        "model": LLM_MODEL,
        "stream": False,
        "options": {
            "temperature": 0
        },
        "prompt": text
    }

    response = requests.post(f"{LLM_HOST}/api/generate", json=data, headers={'Content-Type': 'application/json'}, timeout=MAX_TIMEOUT)
    result = response.json()
    data = result.get("response")
    questions = {
        "text":data,
        "prompt": text,
        "story":story,
        "questions": data.strip().split('\n')
    }
    return questions