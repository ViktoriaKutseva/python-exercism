
colors_list = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
def value(colors: list):
    
    result = ''
    
    for color in colors[:2]:
        result += str(colors_list.index(color))
    return int(result)

print(value((["white", "orange"])))