def card_v(card):
    m = {"A": 14, "K": 13, "Q": 12, "J": 11}
    return m[card[0:-1]] if card[0:-1] in m else int(card[0:-1])


def rank(hand):
    rank, colors = 1, {c[-1] for c in hand.split()}
    vs = [card_v(c) for c in hand.split()]
    f, v = zip(*list(reversed(sorted([(vs.count(i), i) for i in set(vs)]))))
    v = (5, 4, 3, 2, 1) if v == (14, 5, 4, 3, 2) else v

    if v[0] - v[-1] == 4 and len(colors) == 1:
        rank = 9
    elif 4 in f:
        rank = 8
    elif f == (3, 2):
        rank = 7
    elif len(colors) == 1:
        rank = 6
    elif v[0] - v[-1] == 4:
        rank = 5
    elif 3 in f:
        rank = 4
    elif f == (2, 2, 1):
        rank = 3
    elif 2 in f:
        rank = 2

    return (rank, *v)


def best_hands(hands):
    maax, bests = (0, 0), []

    for hand in hands:
        r = rank(hand)
        if r > maax:
            maax = r
            bests = [hand]
        elif r == maax:
            bests.append(hand)

    return bests
