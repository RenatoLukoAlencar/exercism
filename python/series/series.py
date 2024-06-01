def slices(series, length):
    if length == 0:
        raise ValueError("slice length cannot be zero")
    elif length < 0:
        raise ValueError("slice length cannot be negative")
    elif len(series) == 0:
        raise ValueError("series cannot be empty")
    elif len(series) < length:
        raise ValueError("slice length cannot be greater than series length")

    return [series[i:i+length] for i in range(0, len(series)-length+1)]
