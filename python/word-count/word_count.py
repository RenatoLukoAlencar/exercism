def count_words(sentence):
    count, abrev ={},  {"cant": "can't","dont": "don't","youre": "you're"} 

    for word in  sentence.translate(str.maketrans(":!,#%^&$@._\t\n", " "*13)).lower().replace("  ", " ").replace("'", "").split(" "):
        if word != "":
            key = word if word not in abrev.keys() else abrev[word]
            count.setdefault(key, 0)
            count[key] +=1

    return count