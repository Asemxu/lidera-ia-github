def process_text(story_input):
    try:
        # Intenta desescapar si está en formato escapado
        return story_input.encode().decode('unicode_escape')
    except UnicodeDecodeError:
        # Si falla (no está escapado), usa el texto tal cual con UTF-8
        return story_input.encode('utf-8').decode('utf-8')