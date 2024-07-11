class Clock:
    def __init__(self, hour, minute):
        self.minute = minute % 60
        self.hour = (hour + (minute // 60)) % 24

    def __repr__(self):
        return f"Clock({self.hour}, {self.minute})"

    def __str__(self):
        return f"{str(self.hour).rjust(2, '0')}:{str(self.minute).rjust(2, '0')}"

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        self.hour = (((self.hour * 60 + self.minute) + minutes) // 60) % 24
        self.minute = (self.minute + minutes % 60) % 60
        return str(self)

    def __sub__(self, minutes):
        self.hour = (((self.hour * 60 + self.minute) - minutes) // 60) % 24
        self.minute = (self.minute - minutes % 60) % 60
        return str(self)
