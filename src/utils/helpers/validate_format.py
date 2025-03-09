import re

def validate_format(text, pattern):
    match = re.match(pattern, text)
    return bool(match)