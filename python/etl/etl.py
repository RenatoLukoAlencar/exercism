def transform(legacy_data):
    newData = {}
    for key, value in legacy_data.items():
        for letter in value:
            newData.setdefault(letter.lower(), key)

    return newData
