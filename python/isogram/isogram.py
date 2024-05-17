def is_isogram(string):
    newString = string.lower().replace(" ", "").replace("-", "")
    return len(newString.lower()) == len(set(newString))
