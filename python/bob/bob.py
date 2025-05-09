def response(hey_bob: str):
    if hey_bob.isupper() and "?" in hey_bob:
        return "Calm down, I know what I'm doing!" 
    elif hey_bob.isupper() and "?" not in hey_bob:
        return 'Whoa, chill out!'
    elif hey_bob.isspace() or not hey_bob:
        return "Fine. Be that way!" 
    elif hey_bob.strip().endswith('?'):
        return "Sure."
    return "Whatever."
