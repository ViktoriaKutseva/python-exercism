# Score categories.
# Change the values as you see fit.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11

def _get_count(dice):

    count_dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    count = 0   
    dice.sort()
    first_dice = dice[0]
    for n in range(1,7):
        while n == first_dice:
            if first_dice == n:
                count += 1
            dice = dice[1:] 
            if dice:
                first_dice = dice[0]
            else:
                break
        count_dict[n] = count
        count = 0
    print(count_dict)
    return count_dict

def score(dice, category):
    dice_list = [1,2,3,4,5,6]
    count = _get_count(dice)
    if category == YACHT:
        if count[dice[0]] == 5:
            return 50
        return 0
    if category in (1,2,3,4,5,6):
         return dice.count(category) * category
    if category == FULL_HOUSE:
        has_3 = 0
        has_2 = 0
        for i in dice_list:
            if count[i] == 3:
                has_3 += 1
            if count[i] == 2:
                has_2 += 1
            else: 
                has_2 = has_3
        if 1 == has_3 == has_2:
            return sum(dice)
        return 0
    if category == FOUR_OF_A_KIND:
        result = 0
        for i in dice_list:
            if count[i] >= 4:
                result = i * 4   
                return result
            else:
                result += 0
        return 0
    if category == BIG_STRAIGHT:
        result = 0
        for i in dice_list[1:]:
            if count[i] == 1:
                result += 1
            else:
                result += 0
        if result > 4:
            return 30
        return 0
    if category == LITTLE_STRAIGHT:
        result = 0
        if count[6] == 0:
            for i in dice_list:
                if count[i] == 1:
                    result += 1
                else:
                    result += 0
            if result > 4:
                return 30
            return 0
        else:
            return 0
    if category == CHOICE:
        return sum(dice)
        