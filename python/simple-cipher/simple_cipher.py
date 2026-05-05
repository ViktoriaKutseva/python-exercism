import secrets
import random


class Cipher:
    """simple encryption class"""
    def __init__(self, key=None):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.alphabet = list(alphabet)
        self.key = key
        self.key_list = []
        if self.key is None:
            self.key = "".join(
                secrets.choice(alphabet) for i in range(random.randint(100, 120))
            )
        for i in self.key:
            self.key_list.append(self.alphabet.index(i))

    def encode(self, text):
        word_to_code = []
        encoded_text = ""
        key_len = len(self.key_list)
        for i in text:
            word_to_code.append(self.alphabet.index(i))
        for i in range(len(text)):
            rotated_num = (word_to_code[i] + (self.key_list[i % key_len])) % 26
            encoded_text += self.alphabet[rotated_num]
        return encoded_text

    def decode(self, text):
        word_to_code = []
        decoded_text = ""
        key_len = len(self.key_list)
        for i in text:
            word_to_code.append(self.alphabet.index(i))
        for i in range(len(text)):
            rotated_num = (word_to_code[i] - (self.key_list[i % key_len])) % 26
            decoded_text += self.alphabet[rotated_num]
        return decoded_text
