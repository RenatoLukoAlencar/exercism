import random

ATT = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]


class Character:
    def __init__(self):
        for attribute in ATT:
            setattr(self, attribute, self.ability())

        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        test = sorted([random.randint(1, 6) for _ in range(3)])
        return sum(test[1:])


def modifier(n):
    return (n - 10) // 2
