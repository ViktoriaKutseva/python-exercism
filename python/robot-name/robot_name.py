import random
import string

class Robot:
    def __init__(self):
        self.name = self._give_name()
        
    def _give_name(self):
        name = ''
        for _ in range(2):
            name += random.choice(string.ascii_uppercase)
        for _ in range(3):
            name += random.choice(string.digits)
        return name
    
    def reset(self):
        old_name = self.name
        new_name = self._give_name()
        while old_name == new_name:
            new_name = self._give_name()
        self.name = new_name
        return self.name
