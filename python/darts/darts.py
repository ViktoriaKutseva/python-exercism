import math

def score(x, y):
    r_1 = 10 
    r_2 = 5 
    r_3 = 1
    score = 10
    
    distance = math.sqrt(x**2 + y**2)
    if distance > r_1:
        score = 0
        return score
    if  distance > r_2 and distance <= r_1:
        score = 1
        return score
    if distance > r_3 and distance <= r_2:
        score = 5
        return score
    return score
            
    
print(score(-5, 0))