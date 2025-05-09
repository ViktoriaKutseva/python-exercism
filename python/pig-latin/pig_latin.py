def translate(text):
    vowels = "aieou"
    consonants = 'qwrtpsdfghjklzxcvbnym'
    
    if text[0] in vowels or 'xr' in text[:2] or 'yt' in text[:2]:
        text += 'ay'
        return text
    elif  text[0] in consonants and 'qu' not in text:
        while text[0] in consonants:
            text += text[0]
            text = text[1:]
        text += 'ay'
        return text
    elif text[:2] == 'qu' or text[0] in consonants:
        while text[0] in consonants:
            if 'qu' in text[:2]:
                text += 'qu'
                text = text[2:]
                text += 'ay'
                return text
            else:
                text += text[0]
                text = text[1:]
        text += 'ay'
        return text

            
                

# print(translate('apple'))
print(translate('yellow'))
# print(translate("square"))
# print(translate("chair"))
# print(translate("thrush"))
# print(translate("quick"))
print(translate("quick fast run"))


def translate(text):
    vowels = "aeiou"
    
    def translate_word(word):
        if word[0] in vowels or word.startswith(('xr', 'yt')):
            return word + 'ay'
        
        # Find index of first vowel or 'y' acting as vowel
        i = 0
        while i < len(word):
            if word[i:i+2] == 'qu':
                i += 2
                break
            elif word[i] in vowels or (word[i] == 'y' and i != 0):
                break
            i += 1

        return word[i:] + word[:i] + 'ay'
    
    return ' '.join(translate_word(w) for w in text.split())
