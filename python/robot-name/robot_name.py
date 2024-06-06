import random as r 

class Robot:
    def __init__(self):
        self.name = self.generateName()

    def generateName(self):
        n,s  = "1234567890", "ABCDEFGHIJKLMNOPQRSTUVXYWZ"
        return f"{r.choice(s)}{r.choice(s)}{r.choice(n)}{r.choice(n)}{r.choice(n)}"

    def reset(self):
        r.seed(self.name)
        self.name = self.generateName()
