def rows(letter):
    arr, alpha = [], "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n = alpha.index(letter) + 1

    for index in range(0, n):
        midRow = f"{' ' * (n-1-index)}{alpha[index]}{' ' * index}"
        arr.append(midRow + "".join(list(reversed(midRow[:-1]))))

    return arr + list(reversed(arr[:-1]))
