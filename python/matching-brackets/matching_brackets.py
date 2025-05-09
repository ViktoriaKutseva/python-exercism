def is_paired(input_string):
    
    test_string = "{wer234[safsa]}"
    bracket_pairs = ['{}', '[]', '()']
    
    def jopapapa(start_idx = 0, current_pair = None):
        end_idx = 0
        current_string = input_string[start_idx]
        for char in current_string:
            for pair in bracket_pairs:
                if char == pair[0]:
                    jopapapa(current_string.index(char), pair)
    def add_bracket_pair(input_string: str, bracket_pairs, current_pair = None):
        sub_string = ''
        sub_srting_id = 0
        
        for char in input_string:
            for pair in bracket_pairs:
                if char == pair[0]:
                    current_pair = pair
                    sub_string_id = input_string.index(char)
            
        for char in input_string:
            if input_string.index(char) >= sub_srting_id and sub_srting_id != 0:
                sub_string += char
            if char == pair[1]:
                break
        
        add_bracket_pair(sub_string)
            
    
    
    # allowed_symbols = '[{(]})'
    # symbols_open = '[{('
    # symbols_close = ']})'
    # result = ''
    
    # input_string = input_string.strip()
    
    # for char in input_string:
    #     if char in allowed_symbols:
    #         result += char

    # stack = []
    
    # for char in result:
    #     if char in symbols_open:
    #         stack.append(char)
    #     elif char in symbols_close:
    #         if not stack:
    #             return False
    #         last_open = stack.pop()
    #         # Match corresponding opening
    #         if symbols_open.index(last_open) != symbols_close.index(char):
    #             return False

    # return len(stack) == 0
# def is_paired(input_string):
#     allowed_symbols = '[{(]})'
#     symbols_open = '[{('
#     symbols_close = ']})'
#     count_open = 0
#     count_close = 0
#     count = 0
#     symbol = 0
#     result = ''
#     input_string = input_string.strip()
#     for char in input_string:
#         if char in allowed_symbols:
#             result += char
            
#     while count < len(result):
#         for symbol in range(3):
#             if symbols_open[symbol] in result[count]:
#                 # print(symbols_open[symbol])
#                 count_open += 1
#             elif symbols_close[symbol] in result[count]:
#                 print(symbols_close[symbol])

#                 count_close += 1
#             if count_open < count_close:
#                 return False      
#             symbol += 1
#         count += 1
#     if count_open != count_close or result.count('{') != result.count('}') or result.count('[') != result.count(']') or result.count('(') != result.count(')')  :
#         return False
#     return True


print(is_paired("{wer234[safsa])"))
