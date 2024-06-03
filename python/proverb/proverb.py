def proverb(*subs, **kwargs):
    arr, res = list(subs), []

    for index, sub in enumerate(arr):
        if index + 1 != len(arr):
            res.append(
                "For want of a _ the @ was lost.".replace("_", sub).replace(
                    "@", arr[index + 1]
                )
            )
        else:
            mod = f" {kwargs.get('qualifier')} " if kwargs.get("qualifier") else " "
            res.append(f"And all for the want of a{mod}{arr[0]}.")

    return res
