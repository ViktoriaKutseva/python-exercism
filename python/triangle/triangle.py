def equilateral(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if (a + b >= c and b + c >= a and a + c >= b) and a != 0 and b != 0 and c != 0:
        if a == c and a == b and c == b:
            return True
        return False
    return False

def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if (a + b >= c and b + c >= a and a + c >= b) and a != 0 and b != 0 and c != 0:
        if a == b or b == c or  c == a: 
            return True      
        return False
    return False

def scalene(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if (a + b >= c and b + c >= a and a + c >= b) and a != 0 and b != 0 and c != 0:
        if a != c and a != b and c != b:
            return True
        return False
    return False
