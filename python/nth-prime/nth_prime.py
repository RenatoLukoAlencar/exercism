def prime(number):
    if number < 1:
        raise ValueError("there is no zeroth prime")

    arr, current_number = [2], 3

    while len(arr) < number:
        if all(current_number % prime != 0 for prime in arr):
            arr.append(current_number)
        current_number += 2

    return arr[-1]
