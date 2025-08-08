def int_or_float(number):
    if number == int(number):
        return int(number)
    else:
        return float(number)
    
def resistor_label(colors):
    colors_list = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
    result = ''
    zeros_list = {'brown': '0', 'red': '00', 'orange': '000',
    'yellow': '0000', 'green': '00000', 'blue': '000000',
    'violet': '0000000', 'grey': '00000000', 'white': '000000000', 'black': ''}
    
    tolerance_dict = {
    "grey" : "0.05%",
    "violet" : "0.1%",
    "blue" : "0.25%",
    "green" : "0.5%",
    "brown" : "1%",
    "red" : "2%",
    "gold" : "5%",
    "silver" : "10%",
    "black" : ""
    }

    if len(colors) == 1:
        for color in colors:
            result += str(colors_list.index(color))
            result += ' ohms'
            return result

    elif len(colors) == 5:
        for color in colors[:3]:
            result += str(colors_list.index(color))
        for color in colors[3:4]:
                result += zeros_list[color]

    else:
        for color in colors[:2]:
            result += str(colors_list.index(color))     

        for color in colors[2:3]:
            result += zeros_list[color]   

    if int(result) >= 1000000000:
        result = str(int_or_float(int(result)/1000000000))
        result += ' gigaohms'

    elif int(result) >= 1000000:
        result = str(int_or_float(int(result)/1000000))
        result += ' megaohms'

    elif int(result) >= 1000:
        result = str(int_or_float(int(result)/1000))
        result += ' kiloohms'

    else:
        result += ' ohms'

    result += ' ±' + tolerance_dict[colors[-1]]
    
    return result
    