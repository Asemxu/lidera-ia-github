def local_aiquestions_escape_json(value):
    if not isinstance(value, str):
        value = str(value)
    escapers = ["\\", "/", "\"", "\n", "\r", "\t", "\x08", "\x0c"]
    replacements = ["\\\\", "\\/", "\\\"", "\\n", "\\r", "\\t", "\\f", "\\b"]
    result = value
    for escaper, replacement in zip(escapers, replacements):
        result = result.replace(escaper, replacement)
    return result