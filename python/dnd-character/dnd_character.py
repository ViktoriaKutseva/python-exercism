import random


class Character:
    def __init__(self):
        self.strength = self._set_ability()
        self.dexterity = self._set_ability()
        self.constitution = self._set_ability()
        self.intelligence = self._set_ability()
        self.wisdom = self._set_ability()
        self.charisma = self._set_ability()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        return self._set_ability()
    
    def _set_ability(self):
        random_numbers = []
        for i in range(4):
            random_numbers.append(random.randint(1, 6))
        random_numbers.sort()
        random_numbers = random_numbers[1:]
        sum_number = sum(random_numbers)
        return sum_number  
              
              
def modifier(value): 
    return (value - 10) // 2
