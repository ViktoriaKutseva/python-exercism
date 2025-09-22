def recite(start_verse, end_verse):
    days = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']
    gifts = [
        "twelve Drummers Drumming, ",
        "eleven Pipers Piping, ",
        "ten Lords-a-Leaping, ",
        "nine Ladies Dancing, ",
        "eight Maids-a-Milking, ",
        "seven Swans-a-Swimming, ",
        "six Geese-a-Laying, ",
        "five Gold Rings, ",
        "four Calling Birds, ",
        "three French Hens, ",
        "two Turtle Doves, ",
        "and a Partridge in a Pear Tree."
    ]
    temp_list = []
    result = []
    
    for i in range(end_verse - start_verse + 1):
        temp_list = [f'On the {days[start_verse - 1]} day of Christmas my true love gave to me: ']
        count = start_verse
        start_verse +=1
        while count != 0:
            if start_verse == 2:
                temp_list.append('a Partridge in a Pear Tree.')
            else:
                temp_list.append(gifts[-count])
            count -= 1
        result.append(''.join(temp_list))
    return result

