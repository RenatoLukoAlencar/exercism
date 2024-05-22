def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    elif output_base < 2:
        raise ValueError("output base must be >= 2")
    elif not all(map(lambda x: 0 <= x < input_base, digits)):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    elif digits == []:
        return [0]

    res, base10 = [], 0

    for index, value in enumerate(digits):
        base10 += value * (input_base ** (len(digits) - (index + 1)))
    if base10 <= output_base:
        return [base10]
    while base10 > 1:
        res.insert(0, round(round((base10 % output_base) - 0.4)))
        base10 = base10 / output_base

    return res
