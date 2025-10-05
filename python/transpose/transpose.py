def _space_list(text):
    space_list = []
    text_list = text.split('\n')
    count = 0
    for _ in range(len(text_list)):
        space_list.append(len(text_list[count]))
        count += 1
    print(space_list)
    for i in range(len(space_list)):
        if i + 1 < len(space_list):
            if space_list[i] < space_list[-1]:
                space_list[i] = space_list[-1] - space_list[i]
            elif space_list[i] < space_list[i + 1]:
                space_list[i] = space_list[i + 1] - space_list[i]
            else:
                space_list[i] = 0
    space_list[-1] = 0
    print(space_list)
    return space_list

def _fix_spaces(text):
    fixed_list = []
    text_list = text.split('\n')
    space_list = _space_list(text)  
    for i in range(len(text_list)):
        temp_text = str(text_list[i]) + ' ' * (space_list[i])
        fixed_list.append(temp_text)
    return fixed_list

def transpose(text):
    text_list = text.split('\n')
    text_list.sort()
    space_list = _space_list(text)  
    fixed_list = _fix_spaces(text)
    len_list = len(text_list)
    max_cols = max(len(row) for row in fixed_list)
    transpose = ''
    for i in range(max_cols) :
        for n in range(len_list):
            s = fixed_list
            if i < len(s[n]):        
                transpose += str(s[n][i])
            else:
                if space_list[0] != 0:
                    transpose += ' '
                else:
                    transpose += ''
        transpose += '\n'  
    return transpose.strip()


