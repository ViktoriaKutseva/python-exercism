def transpose(text):
    text_list = text.split('\n')
    find_longest = 0
    fixed_list = []
    transpose = ''
    for i in range(len(text_list)):
        if len(text_list[i]) > find_longest:
            find_longest = len(text_list[i])
        else:
            find_longest = find_longest
    for i in range(len(text_list)):
        temp_text = ''
        if len(text_list[i]) < find_longest:
            temp_text = str(text_list[i]) + ' ' * (find_longest-len(text_list[i]))
            fixed_list.append(temp_text)
        else:
            fixed_list.append(str(text_list[i]))
    print(fixed_list)
    for i in range(find_longest):
        for n in range(len(fixed_list)):
            s = fixed_list
            if s[n][i]:
                temp_text = str(s[n][i])
                transpose += str(s[n][i])
            else:
                transpose += ''
        if i + 1 == find_longest:
            transpose = transpose
        else:
            transpose += '\n'
            
    return transpose.strip()


text = "The longest line.\nA long line.\nA longer line.\nA line."
expected = "TAAA\nh   \nelll\n ooi\nlnnn\nogge\nn e.\nglr\nei \nsnl\ntei\n .n\nl e\ni .\nn\ne\n."

print(transpose(text).__repr__())
print('puk')
print(expected.__repr__())



def _space_list(text):
    space_list = []
    text_list = text.split('\n')
    count = 0
    for _ in range(len(text_list)):
        space_list.append(len(text_list[count]))
        count += 1
    for i in range(len(space_list)):
        if i + 1 < len(space_list):
            if space_list[i] < space_list[i + 1]:
                space_list[i] = space_list[i + 1] - space_list[i]
            else:
                space_list[i] = 0
    space_list[-1] = 0
    return space_list

def _fix_spaces(text):
    fixed_list = []
    text_list = text.split('\n')
    find_longest = len(text_list[0])
    longest_index = 0
    for i in range(len(text_list)):
            if len(text_list[i]) > find_longest:
                find_longest = len(text_list[i])
                longest_index = i
            else:
                find_longest = find_longest
    print(longest_index)
    text_len = len(text_list[0])
    for i in range(len(text_list)):
        if i + 1 < len(text_list):
            text_len = len(text_list[i + 1])
        else: 
            text_len = text_len    
        temp_text = ''
        if len(text_list[i]) < text_len:
            temp_text = str(text_list[i]) + ' ' *(text_len - len(text_list[i]))
            fixed_list.append(temp_text)
        elif  longest_index < i:
            fixed_list.append(str(text_list[i]))
            
        else:
            temp_text = str(text_list[i]) + ' ' * (find_longest-len(text_list[i]))
            fixed_list.append(temp_text)
    return fixed_list

# def transpose(text):
#     fixed_list = _fix_spaces(text)
#     transpose = ''
#     print(fixed_list)
#     for i in range(len(fixed_list[0])):
#         for n in range(len(fixed_list)):
#             s = fixed_list
#             if i < len(s[n]):
#                 if s[n][i]:
#                     temp_text = str(s[n][i])
#                     transpose += str(s[n][i])
#                 else:
#                     transpose += ''
#             else:
#                 break
#         if i + 1 == fixed_list[0][0]:
#             transpose = transpose
#         else:
#             transpose += '\n'
            
#     return transpose.strip()


text = "11\n2\n3333\n444\n555555\n66666"
expected = "123456\n1 3456\n  3456\n  3 56\n    56\n    5"

print(transpose(text).__repr__())
print('puk')
print(expected.__repr__())