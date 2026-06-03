import math


def normalize_plaintext(plain_text):
    return ''.join(c.lower() for c in plain_text if c.isalnum())


def cipher_text(plain_text):
    normalize_text = normalize_plaintext(plain_text)
    if normalize_text:
        text_length = len(normalize_text)
        square_len = math.ceil(math.sqrt(text_length))
        chunk_len = round(len(normalize_text) / square_len)
        square_text = ''
        for i in range(square_len):
            encoded_chunk = normalize_text[i::square_len]
            square_text += encoded_chunk + ' '
            if len(encoded_chunk) < chunk_len:
                gap_length = chunk_len - len(encoded_chunk)
                square_text += ' ' * gap_length
        square_text = square_text[:-1]
        return square_text
    return ''
