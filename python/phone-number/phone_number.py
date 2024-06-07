class PhoneNumber:
    def __init__(self, number):
        for n in str(number):
            if n in "@:!":
                raise ValueError("punctuations not permitted")
            elif n.isalpha():
                raise ValueError("letters not permitted")
        self.number = "".join([char if char.isdigit() else "" for char in str(number)])
        self.area_code = self.number[-10:-7]
        self.exchange_code = self.number[-7:-4]
        self.subscriber_number = self.number[-4:]

        if len(self.number) == 11 and self.number[0] != "1":
            raise ValueError("11 digits must start with 1")
        elif self.number[0] == "1":
            self.number = self.number[1:]
        elif len(self.number) > 11:
            raise ValueError("must not be greater than 11 digits")
        if len(number) < 10:
            raise ValueError("must not be fewer than 10 digits")
        elif self.area_code[0] == "1":
            raise ValueError("area code cannot start with one")
        elif self.area_code[0] == "0":
            raise ValueError("area code cannot start with zero")
        elif self.exchange_code[0] == "1":
            raise ValueError("exchange code cannot start with one")
        elif self.exchange_code[0] == "0":
            raise ValueError("exchange code cannot start with zero")

    def pretty(self):
        return f"({self.area_code})-{self.exchange_code}-{self.subscriber_number}"
