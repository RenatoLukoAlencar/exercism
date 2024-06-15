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
    res = 0
    match category:
        case 0:
            res = 50 if len(set(dice)) == 1 else 0
        case 7:
            res = sum(dice) if len(set(dice)) == 2 else 0
        case 8:
            sete = set(dice)
            if len(sete) == 2:
                first, second = sete
                countFirst = dice.count(first)
                countSecond = dice.count(second)
                if countFirst == 4 or countSecond == 4:
                    res = (
                        countFirst * first if countFirst == 4 else countSecond * second
                    )
                else:
                    res = 0

            else:
                res = 0

        case 9 | 10:
            arr_sort, sete = sorted(dice), set(dice)
            print(f"arr_sort: {arr_sort}")
            print(f"sum: {sum(dice)}")

            res = 30 if (len(sete) == 5) else 0

        case 11:
            res = sum(dice)
        case 1 | 2 | 3 | 4 | 5 | 6:
            res = dice.count(category) * category
    return res
