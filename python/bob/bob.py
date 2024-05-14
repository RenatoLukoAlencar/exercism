def response(hey_bob):
    res, sbob, difUpLow = (
        "Whatever.",
        hey_bob.strip(),
        hey_bob.upper() != hey_bob.lower(),
    )

    if sbob == "":
        res = "Fine. Be that way!"
    elif sbob[-1] == "?" and sbob.upper() == sbob and difUpLow:
        res = "Calm down, I know what I'm doing!"
    elif sbob[-1] == "?":
        res = "Sure."
    elif sbob == sbob.upper() and difUpLow:
        res = "Whoa, chill out!"

    return res
