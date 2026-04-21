def line_up(name, number):
    exception = ("11", "12", "13")
    if str(number)[-2:] not in exception:
        if number % 10 == 1:
            suffix = "st"
        elif number % 10 == 2:
            suffix = "nd"
        elif number % 10 == 3:
            suffix = "rd"
        else:
            suffix = "th"
    else:
        suffix = "th"
    return f"{name}, you are the {number}{suffix} customer we serve today. Thank you!"
