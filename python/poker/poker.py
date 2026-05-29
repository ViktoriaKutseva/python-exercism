from collections import Counter

ROYAL_FLUSH = 10000
FOUR_OF_A_KIND = 9000
FULL_HOUSE = 8000
FLUSH = 7000
STRAIGHT = 6000
THREE_OF_A_KIND = 5000
TWO_PAIRS = 4000 
PAIR = 3000

def _is_straight(hand) -> int | bool:
    if hand == [2,3,4,5,14]:
        return 2
    for i in range(1, len(hand)):
        if hand[i] == hand[i - 1] + 1:
            continue
        return False
    max_index = hand.index(max(hand))
    return hand[max_index]

def _is_flush(hand) -> bool:
    for i in range(1, len(hand)):
        if hand[i][-1] == hand[i - 1][-1]:
            continue
        return False
    return True

def _is_foak(hand) -> list:
    counts = Counter(hand)
    return [card for card, count in counts.items() if count == 4]

def _is_thoak(hand) -> list:
    counts = Counter(hand)
    return [card for card, count in counts.items() if count == 3]

def _is_toak(hand) -> list:
    counts = Counter(hand)
    return [card for card, count in counts.items() if count == 2]

def best_hands(hands) -> list:
    face_to_value = {
        "2": 2, "3": 3, "4": 4, "5": 5, 
        "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, 
        "J": 11, "Q": 12, "K": 13, "A": 14
                     }
    sorted_by_value = []
    hands_values = []
    winner = []
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
            hand_value_calc += ROYAL_FLUSH + _is_straight(sorted_by_value)

        elif _is_foak(sorted_by_value):
            hand_value_calc += FOUR_OF_A_KIND + sum(_is_foak(sorted_by_value)) * 5 + sorted_by_value[-1]
            
        elif _is_thoak(sorted_by_value) and _is_toak(sorted_by_value):
            hand_value_calc += FULL_HOUSE + (sum(_is_thoak(sorted_by_value)) * 2) + sum(_is_toak(sorted_by_value))

        elif _is_flush(split_hand):
            hand_value_calc += FLUSH + sum(sorted_by_value)

        elif _is_straight(sorted_by_value):
            hand_value_calc += STRAIGHT + _is_straight(sorted_by_value)

        elif _is_thoak(sorted_by_value):
            hand_value_calc += THREE_OF_A_KIND + sum(_is_thoak(sorted_by_value)) * 5 + sorted_by_value[0] + sorted_by_value[1]*2

        elif _is_toak(sorted_by_value):
            pairs = _is_toak(sorted_by_value)
            left_value = [card for card in sorted_by_value if card not in pairs]
            if len(pairs) == 2:
                hand_value_calc += TWO_PAIRS + pairs[-1] * 5 + pairs[0] + sum(left_value)
            else:
                hand_value_calc += PAIR + pairs[-1] * 5 + sum(left_value)
        else:
            hand_value_calc += sorted_by_value[-1] * 50 + sorted_by_value[-2] * 10 + sorted_by_value[-3] * 5 + sorted_by_value[-4] * 2 + sorted_by_value[-5]
        hands_values.append(hand_value_calc)
    for i, value in enumerate(hands_values):
        if value == max(hands_values):
            winner.append(hands[i])
    return winner
