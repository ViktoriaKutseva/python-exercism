import re

class PhoneNumber:
    def __init__(self, number):
        self.number = number
        self.number = self._make_valid()
        
    def _make_valid(self):
        self.number = self._check_validity()
        number = re.findall(r'\d', self.number)
        number = ''.join(number) 
        if len(number) == 11:
            number = number[1:]
        self.area_code = number[0:3]
        return number
    
    def _check_validity(self):
        check_for_letters = re.findall(r'[a-zA-Z]', self.number)        
        if check_for_letters:
            raise ValueError ("letters not permitted")
        number = re.findall(r'\d', self.number)
        if len(number) > 11:
            raise ValueError('must not be greater than 11 digits')
        if len(number) < 10 and len(self.number) > 10:
            raise ValueError("punctuations not permitted")
        if len(number) < 10:
            raise ValueError('must not be fewer than 10 digits')   
        if len(number) == 11 and number[0] != '1':
            raise ValueError('11 digits must start with 1')   
        if number[-10] == '0':
            raise ValueError('area code cannot start with zero')
        if number[-10] == '1':
            raise ValueError('area code cannot start with one')
        if number[-7] == '0':
            raise ValueError('exchange code cannot start with zero')
        if number[-7] == '1':  
            raise ValueError('exchange code cannot start with one')
        number = ''.join(number) 
        return number    

    def pretty(self):
        n = self.number
        number = f'({n[0:3]})-{n[3:6]}-{n[6:]}'
        return number

