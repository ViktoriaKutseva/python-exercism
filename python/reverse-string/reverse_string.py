def reverse(text):
    reversed_text = [text[-i - 1] for i in range(len(text))]
    return ''.join(reversed_text)
