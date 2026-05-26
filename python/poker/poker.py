
def _is_straight(hand):
    if hand == [2,3,4,5,14]:
        return 2
    for i in range(1, len(hand)):
        if hand[i] == hand[i - 1] + 1:
            continue
        return False
    max_index = hand.index(max(hand))
    return hand[max_index]

def _is_flush(hand):
    for i in range(1, len(hand)):
        if hand[i][-1] == hand[i - 1][-1]:
            continue
        return False
    return True

def _is_foak(hand):
    for card in hand:
        if hand.count(card) == 4:
            return card
    return False

def _is_thoak(hand):
    for card in hand:
        if hand.count(card) == 3:
            return card
    return False

def _is_toak(hand):
    result = []
    for card in hand:
        if hand.count(card) == 2:
            result.append(card)
            hand = [i for i in hand if i != card]
    if result:
        return result
    return result

def best_hands(hands):
    face_to_value = {"2" : 2, "3": 3, "4": 4, "5": 5, "6" : 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q" : 12, "K": 13, "A": 14}
    sorted_by_value = []
    hands_values = []
    for hand in hands:
        hand_value_calc = 0
        sorted_by_value = []
        split_hand = hand.split()

        for card in split_hand:
            if len(card) == 2:
                sorted_by_value.append(face_to_value[card[0]])
            else:
                sorted_by_value.append(10)

        sorted_by_value = sorted(sorted_by_value)

        if _is_flush(split_hand) and _is_straight(sorted_by_value):
            hand_value_calc += 10000 + _is_straight(sorted_by_value)

        elif _is_foak(sorted_by_value):
            hand_value_calc += 9000 + _is_foak(sorted_by_value)*5 + sorted_by_value[-1]
            
        elif _is_thoak(sorted_by_value) and _is_toak(sorted_by_value):
            hand_value_calc += 8000 + (_is_thoak(sorted_by_value) * 2) + sum(_is_toak(sorted_by_value))

        elif _is_flush(split_hand):
            hand_value_calc += 7000 + sum(sorted_by_value)

        elif _is_straight(sorted_by_value):
            hand_value_calc += 6000 + _is_straight(sorted_by_value)

        elif _is_thoak(sorted_by_value):
            hand_value_calc += 5000 + _is_thoak(sorted_by_value)*5 + sorted_by_value[0] + sorted_by_value[1]*2

        elif _is_toak(sorted_by_value):
            pairs = _is_toak(sorted_by_value)
            left_value = [card for card in sorted_by_value if card not in pairs]
            if len(pairs) == 2:
                hand_value_calc += 4000 + pairs[-1]*5 + pairs[0] + sum(left_value)
            else:
                hand_value_calc += 3000 + pairs[-1]*5 + sum(left_value)
        else:
            hand_value_calc += sorted_by_value[-1]*50 + sorted_by_value[-2]*10 + sorted_by_value[-3]*5 + sorted_by_value[-4]*2 + sorted_by_value[-5]

        hands_values.append(hand_value_calc)
        winner = []
    print(hands_values)
    for i, value in enumerate(hands_values):
        if value == max(hands_values):
            winner.append(hands[i])
        continue
    return winner
