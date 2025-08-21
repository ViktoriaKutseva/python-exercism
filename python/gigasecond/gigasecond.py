from datetime import timedelta

def add(moment):
    gigasecond = timedelta(seconds = 1e9)
    result = moment +  gigasecond
    return result
