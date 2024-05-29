def is_paired(input_string):
    newString = "".join(bracket for bracket in input_string if bracket in "{}[]()")

    while True:
        if "()" in newString:
            newString = newString.replace("()", "")
        elif "{}" in newString:
            newString = newString.replace("{}", "")
        elif "[]" in newString:
            newString = newString.replace("[]", "")
        else:
            return True if newString == "" else False
