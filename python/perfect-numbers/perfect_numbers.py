def classify(number):
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    ns = []
    for n in range(1, number):
        if number % n == 0:
            ns.append(n)

    return (
        "perfect"
        if sum(ns) == number
        else "abundant" if sum(ns) > number else "deficient"
    )
