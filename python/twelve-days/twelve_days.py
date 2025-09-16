def recite(start_verse, end_verse):
    time = ['first', 'second', 'third', 'fourth', 'fifth']
    n = 0
    resulted_verse = []
    result = []
    if start_verse == end_verse:
        n = start_verse
        verse = [f'On the {time[n]} day of Christmas my true love gave to me:', 
                'twelve Drummers Drumming,', 'eleven Pipers Piping, ten Lords-a-Leaping,',
                'nine Ladies Dancing,', 'eight Maids-a-Milking,', 'seven Swans-a-Swimming,',
                'six Geese-a-Laying,', 'five Gold Rings,', 'four Calling Birds,', 'three French Hens,', 
                'two Turtle Doves,', 'and a Partridge in a Pear Tree.']
        resulted_verse.append(verse[0])
        resulted_verse += (verse[12-n:])
    resulted_verse = str(resulted_verse)
    resulted_verse = resulted_verse.replace("',", "").replace('[', '').replace(']', '').replace("'", "")
    result.append(resulted_verse)

    return result

print(recite(3,3))