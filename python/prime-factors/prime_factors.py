def factors(value):
    res = []

    if value == 1:
        return res

    current = value
    test = primes()
    for i in test:
        while current % i == 0:
            res.append(i)
            current /= i

    return res


def primes():  # simple sieve of multiples
    n = 10000
    odds = range(3, n + 1, 2)
    sieve = set(sum([list(range(q * q, n + 1, q + q)) for q in odds], []))
    return [2] + [p for p in odds if p not in sieve] + [894119]
