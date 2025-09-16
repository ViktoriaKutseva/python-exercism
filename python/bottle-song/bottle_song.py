def recite(start, take=1):
    poem = []
    n_upper_dict = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6 : 'Six', 7 : 'Seven', 8 : 'Eight', 9: 'Nine', 10: 'Ten'}
    n_lower_dict = {0: 'no', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6 : 'six', 7 : 'seven', 8 : 'eight', 9: 'nine', 10: 'ten'}
    while take != 0:
        if start == 1:
            bottle = 'bottle'
        else:
            bottle = 'bottles'
        poem.append(f"{n_upper_dict[start]} green {bottle} hanging on the wall,")
        poem.append(f"{n_upper_dict[start]} green {bottle} hanging on the wall,")
        poem.append("And if one green bottle should accidentally fall,")
        start -= 1
        if start == 1:
            bottle = 'bottle'
        else:
            bottle = 'bottles'        
        poem.append(f"There'll be {n_lower_dict[start]} green {bottle} hanging on the wall.")
        if take > 1:
            poem.append('')
        take -= 1
    return poem
        