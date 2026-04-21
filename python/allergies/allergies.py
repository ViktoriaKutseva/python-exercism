class Allergies:

    def __init__(self, score):
        self.score = score
        self.allergies_map = {
            1: "eggs",
            2: "peanuts",
            4: "shellfish",
            8: "strawberries",
            16: "tomatoes",
            32: "chocolate",
            64: "pollen",
            128: "cats",
        }

    def allergic_to(self, item):
        if self.score < 0:
            return False
        if self.score > 255:
            return True
        for bit, allergen in self.allergies_map.items():
            if allergen == item:
                return (self.score & bit) != 0
        return False

    @property
    def lst(self):
        pass

