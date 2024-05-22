def commands(binary_str):
    secret, code = [], ["reverse", "jump", "close your eyes", "double blink", "wink"]

    for index, value in enumerate(binary_str):
        if index != 0 and value == "1":
            secret.append(code[index])

    return secret if binary_str[:1] != "0" else list(reversed(secret))
