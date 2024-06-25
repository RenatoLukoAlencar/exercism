import random


class Cipher:
    alpha = "abcdefghijklmnopqrstuvwxyz"
    secret = ""

    def __init__(self, key=None):

        if key == None:
            self.secret = random.choice(self.alpha)

        self.key = key if key != None else "".join([self.secret for _ in range(100)])
        self.text = ""
        self.last = 0

    def encode(self, text):
        current = list(text)
        for i, letter in enumerate(text):
            l_i = self.alpha.index(letter)
            add_i = self.alpha.index(self.key[self.last])
            r_i = (
                l_i + add_i
                if l_i + add_i < len(self.alpha)
                else l_i + add_i - len(self.alpha)
            )
            self.last = self.last + 1 if self.last + 1 != len(self.key) else 0
            current[i] = self.alpha[r_i]

        return "".join(current)

    def decode(self, text):
        current = list(text)
        for i, letter in enumerate(text):
            l_i = self.alpha.index(letter)
            add_i = self.alpha.index(self.key[self.last])
            r_i = l_i - add_i if l_i - add_i >= 0 else l_i - add_i + len(self.alpha)
            self.last = self.last + 1 if self.last + 1 != len(self.key) else 0
            current[i] = self.alpha[r_i]

        return "".join(current)
