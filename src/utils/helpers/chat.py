from src.utils.constants.prompt import   GETPROMPTBOT

def format_system_message(context):
    system_prompt =GETPROMPTBOT(context)
    return system_prompt