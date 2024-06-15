# Score categories.
# Change the values as you see fit.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    r, s = 0, set(dice)
    match category:
        case 0:
            r = 50 if len(s) == 1 else 0
        case 7:
            r = sum(dice) if len(s) == 2 and dice.count(dice[0]) in [2, 3] else 0
        case 8:
            if len(s) != 1:
                for key, value in {elem: dice.count(elem) for elem in s}.items():
                    if value >= 4:
                        r = key * 4
            else:
                r = s.pop() * 4
        case 9:
            r = 30 if (len(s) == 5) and (sum(dice) == 15) else 0
        case 10:
            r = 30 if (len(s) == 5) and (sum(dice) == 20) else 0
        case 11:
            r = sum(dice)
        case 1 | 2 | 3 | 4 | 5 | 6:
            r = dice.count(category) * category
    return r
