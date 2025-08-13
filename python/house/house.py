def recite(start_verse, end_verse):
    start_sentence = ['This is the house that Jack built.', 
                      'This is the malt', 
                      'This is the rat', 
                      'This is the cat',
                      'This is the dog',
                      'This is the cow with the crumpled horn',
                      'This is the maiden all forlorn',
                      'This is the man all tattered and torn',
                      'This is the priest all shaven and shorn',
                      'This is the rooster that crowed in the morn',
                      'This is the farmer sowing his corn',
                      'This is the horse and the hound and the horn'
                      ]
    text = ['',
             'that lay in the house that Jack built.',
            'that ate the malt', 
            'that killed the rat', 
            'that worried the cat', 
            'that tossed the dog',
            'that milked the cow with the crumpled horn',
            'that kissed the maiden all forlorn',
            'that married the man all tattered and torn',
            'that woke the priest all shaven and shorn',
            'that kept the rooster that crowed in the morn',
            'that belonged to the farmer sowing his corn'
            ]
    recite_text = []
    recited_text = []
    count = start_verse

    if start_verse == end_verse:
        recite_text.append(start_sentence[start_verse - 1])
        start_verse -= 1
        while end_verse != 0:
            recite_text.append(text[end_verse - 1])
            end_verse -= 1
        recite_text = ' '.join(recite_text)
        recite_text = recite_text[:-1]
        recited_text.append(recite_text)
        return recited_text

    else:
        while start_verse <= end_verse:
            recite_text.append(start_sentence[start_verse - 1])
            count = start_verse
            while count != 0:
                recite_text.append(text[count - 1])
                count -=1
                if count == 0:
                    recite_text.append(',')
            start_verse += 1      
        recite_text = ' '.join(recite_text)
        recite_text = recite_text.split(',')
        recite_text = [line.strip() for line in recite_text if line.strip()]

        return recite_text
