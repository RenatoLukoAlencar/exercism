def translate(text):
    arr, vow = text.split(" "), "aeiou"

    for i, v in enumerate(arr):
        if v[0] in vow or (v[0] in "yx" and v[1] in "tr"):
            arr[i] = arr[i] + "ay"
        elif v[1] == "y":
            arr[i] = arr[i][1:] + arr[i][:1] + "ay"
        elif (v[0] not in vow and v[1] not in vow and v[2] not in vow) or (
            v[0] not in vow and v[1:3] == "qu"
        ):
            arr[i] = (
                arr[i][v.index("y") :] + arr[i][: v.index("y")] + "ay"
                if "y" in v[:3]
                else arr[i][3:] + arr[i][:3] + "ay"
            )
        elif v[:2] == "qu" or v[1] not in vow:
            arr[i] = arr[i][2:] + arr[i][:2] + "ay"
        else:
            arr[i] = arr[i][1:] + arr[i][:1] + "ay"
    return " ".join(arr)
