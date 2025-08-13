def find_anagrams(word, candidates):
    word = word.lower()
    lower_candidates = []
    result = []
    count = 0
    chars = 0
    letters = word
    for i in range(len(candidates)):
        if len(candidates[i]) == len(word) and not(candidates[i].lower() == word):
            lower_candidates.append(candidates[i].lower())
        else:
            continue
        for char in lower_candidates[chars]:
            if char in letters:
                count +=1
            index = letters.find(char)
            letters = letters[:index] + letters[index+1:]            
        if count == len(word):
            result.append(candidates[i])
        chars += 1
        count = 0
        letters = word
    return result

