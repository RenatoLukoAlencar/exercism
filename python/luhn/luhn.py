class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")

    def valid(self):
        if self.card_num.isdigit() and self.card_num != "0":
            temp = list(map(lambda x: int(x), list(self.card_num)))
            temp.reverse()

            for key, value in enumerate(temp):
                if key % 2 != 0:
                    temp[key] = value * 2 if value * 2 < 10 else (value * 2) - 9

            return sum(temp) % 10 == 0
        else:
            return False
