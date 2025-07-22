def label(colors):
    colors_list = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
    result = ''
    zeros_list = {'black': '', 'brown': '0', 'red': '00', 'orange': '000',
    'yellow': '0000', 'green': '00000', 'blue': '000000',
    'violet': '0000000', 'grey': '00000000', 'white': '000000000'}

    for color in colors[:-1]:
        result += str(colors_list.index(color))

    for color in colors[2:3]:
        result += zeros_list[color]

    if result == '000':
        result = "jopa"
        return result 
    
    if result[0] == '0':
        result = result[1:] + ' ohms'
        return result

    if int(result) % 1000000000 == 0:
        result = result[:-9]
        result += ' gigaohms'
        return result

    if int(result) % 1000000 == 0:
        result = result[:-6]
        result += ' megaohms'
        return result

    if int(result) % 1000 == 0:
        result = result[:-3]
        result += ' kiloohms'
        return result

    if int(result) % 100 == 0:
        result = result[:-2]
        result += ' hectoohms'
        return result
        
    else:
        result += ' ohms'
        return result
