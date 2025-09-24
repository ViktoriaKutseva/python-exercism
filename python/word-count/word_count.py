import re 
from collections import Counter

def count_words(sentence):
    sentence = sentence.strip().strip('"\'').lower()
    sentence = re.findall(r"[a-z0-9]+(?:'[a-z0-9]+)*", sentence)
    counter = Counter(sentence) 
    return counter

