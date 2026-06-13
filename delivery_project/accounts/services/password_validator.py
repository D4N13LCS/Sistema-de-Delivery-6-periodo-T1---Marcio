import re

MIN_PASSWORD_LENGTH = 8
UPPERCASE_PATTERN = r"[A-Z]"
LOWERCASE_PATTERN = r"[a-z]"
SPECIAL_CHARACTER_PATTERN = r"[\W_]"


def senha_valida(password):

    if len(password) < MIN_PASSWORD_LENGTH:
        return False

    if not re.search(UPPERCASE_PATTERN, password):
        return False

    if not re.search(LOWERCASE_PATTERN, password):
        return False

    if not re.search(SPECIAL_CHARACTER_PATTERN, password):
        return False

    return True