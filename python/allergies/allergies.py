class Allergies:

    def __init__(self, score):
        self.allergy_list = []
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
        score = score%256

        for i in reversed(self.allergies_map.keys()):
            if score >= i:
                self.allergy_list.append(self.allergies_map[i])
                score = score % i 
                print (score)
            else:
                continue

    def allergic_to(self, item):
        if item in self.allergy_list:
            return True
        return False

    @property
    def lst(self):
        return self.allergy_list

