def score(word):
    values_dict = {1: 'AEIOULNRST', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
    score_dict = {}
    for key, value in values_dict.items():
        for char in value:
            score_dict[char] = key
    result = 0
    for char in word:
        result += score_dict[char.upper()]        
    return result
