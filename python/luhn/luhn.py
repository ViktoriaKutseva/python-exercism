
class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        valid_numbers = '0123456789'
        number_to_check = 0
        reversed_card = ''.join(reversed(self.card_num))
        reversed_card = ''.join(reversed_card.split())
        for number in range(len(reversed_card)):
            if reversed_card[number] in valid_numbers:
                n = int(reversed_card[number])
            if (reversed_card[number] not in valid_numbers) or (len(reversed_card) == 1):
                return False
            elif number%2 == 0 or number == 0:
                number_to_check += n
            else:
                n *= 2
                if n > 9:
                    n -= 9 
                    number_to_check += n 
                else: 
                    number_to_check += n
        if number_to_check % 10 == 0:
            return True
        return False            
        