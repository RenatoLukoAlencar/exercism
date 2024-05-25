def find(search_list, value):
    try:
        search_list.index(value)
    except:
        raise ValueError("value not in array")

    current = search_list
    finalIndex, found = 0, False

    while not found:
        middleIndex = int(len(current) / 2)
        middleValue = current[middleIndex]

        if value >= middleValue:
            finalIndex += middleIndex

        if value == middleValue:
            found = True
            pass

        current = (
            current[middleIndex:] if value > middleValue else current[:middleIndex]
        )

    return finalIndex
