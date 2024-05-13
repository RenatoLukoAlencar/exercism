def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    arr = [number]

    while arr[-1] != 1:
        arr.append(arr[-1] / 2 if arr[-1] % 2 == 0 else (arr[-1] * 3) + 1)

    return len(arr) - 1
