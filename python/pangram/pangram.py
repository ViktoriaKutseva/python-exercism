def is_pangram(sentence):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    lower_sentence = sentence.lower()
    for letter in alphabet:
        if letter not in lower_sentence:
            return False
    return True

print(is_pangram("a quick movement of the enemy will jeopardize five gunboats"))
