class Clock:
    def __init__(self, hour, minute):
        total_minutes = hour * 60 + minute
        self.hour = (total_minutes // 60) % 24
        self.minute = total_minutes % 60

    def __repr__(self):
        return f"Clock({self.hour}, {self.minute})" 

    def __str__(self):
        hour = str(self.hour)
        minute = str(self.minute)
        if len(hour) == 1:
            hour = "".join(["0", hour])
        if len(minute) == 1:
            minute = "".join(["0", minute])
        return f"{hour}:{minute}"

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes)
    
    def __sub__(self, minutes):
        return Clock(self.hour, self.minute - minutes)
