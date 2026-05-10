from collections import Counter

def _is_straight(hand):
    for i in range(1, len(hand)):
        if hand[i] == hand[i - 1] + 1:
            continue
        return False
    return True

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
        hand = hand.split()

        for card in hand:
            if len(card) == 2:
                sorted_by_value.append(face_to_value[card[0]])
            else:
                sorted_by_value.append(10)

        sorted_by_value = sorted(sorted_by_value)

        if _is_flush(hand) and _is_straight(sorted_by_value):
            hand_value_calc += 1111 + sorted_by_value[-1]

        elif _is_foak(sorted_by_value):
            hand_value_calc += 888 + _is_foak(sorted_by_value)
            
        elif _is_thoak(sorted_by_value) and _is_toak(sorted_by_value):
            hand_value_calc += 777 + (_is_thoak(sorted_by_value) * 2)

        elif _is_flush(hand):
            hand_value_calc += 666 + sorted_by_value[-1]

        elif _is_straight(sorted_by_value):
            hand_value_calc += 555 + sorted_by_value[-1]

        elif _is_thoak(sorted_by_value):
            hand_value_calc += 444 + _is_thoak(sorted_by_value)

        elif _is_toak(sorted_by_value):
            pairs = _is_toak(sorted_by_value)
            if len(pairs) == 2:
                hand_value_calc += 333 + pairs[-1]*2 + pairs[0]
            else:
                hand_value_calc += 222 + pairs[0]
                 
        else:
            hand_value_calc += sorted_by_value[-1]

        hands_values.append(hand_value_calc)
        max_index = hands_values.index(max(hands_values))
        print(hands_values)
    return [hands[max_index]]
print(best_hands(["KC AH AS AD AC", "10C JC QC KC AC"]))

# print(_is_toak([2,2,3,3,4]))

## points for the cards : 
# royal_flush = 1111
# straight_flush = 999 + highest_card_value
# four_of_a_kind = 888 + card_four_value
# full_house = 777 + three_card_valuex2 + two_cards_value
# flush = 666 + highest_value_card
# straight = 555 + highest_value_card
# three = 444 + highest_value_card
# two_pairs = 333 + highest_value_1 + highest_value_2
# pair = 222 + highest_pair_value
# high_card = high_card

