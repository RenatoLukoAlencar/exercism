def flatten(iterable):
    newArr = []
    for i in iterable:
        if type(i) == list:
            for t in unzip(i):
                newArr.append(t) if t or t == 0 else False
        else:
            newArr.append(i) if i or i == 0 else False

    return newArr


def unzip(arr):
    for i in arr:
        if type(i) == list:
            for ele in unzip(i):
                yield ele
        else:
            yield i
