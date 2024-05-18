def answer(question):
    arr = (
        question.replace("by ", "").replace("?", "").replace("What is ", "").split(" ")
    )
    try:
        if len(arr) == 1 and arr[0].isdigit():
            return int(arr[0])

        if arr[0] == "Who" or arr.count("cubed") > 0:
            raise NameError
        elif len(arr) < 3 or len(arr) % 2 == 0:
            raise Exception

        res = int(arr[0])
        trade = {"minus": "-", "plus": "+", "multiplied": "*", "divided": "/"}
        for i in range(1, len(arr), 2):
            n = int(arr[i + 1])
            res = eval(f"{res}{trade[arr[i]]}{n}")

        return int(res)
    except NameError:
        raise ValueError("unknown operation")
    except:
        raise ValueError("syntax error")
