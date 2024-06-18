def triplets_with_sum(number):
    res = []
    for a in range(1, int(number / 3)):
        for b in range(a + 1, int(number / 2)):
            c = number - a - b
            if a * a + b * b == c * c:
                res.append([a, b, c])

    return res
