def sum_of_multiples(limit, multiples):
    arr = []
    for number in multiples:
        if number != 0:
            for i in range(limit):
                if i % number == 0:
                    arr.append(i)

    return sum(set(arr))
