def rebase(input_base, digits, output_base):
    print(f"input_base: {input_base}, \ndigits: {digits}, \noutput_base: {output_base}")

    digitsArr = []

    for index, value in enumerate(str(digits)):
        print(f"index: {index}, value: {value}")
        i = index
        digitsArr.append(f"({value} x {input_base}^{len(str(digits)) +(i - 1)})")

    print(" + ".join(digitsArr))


rebase(2, 101010, 4)
