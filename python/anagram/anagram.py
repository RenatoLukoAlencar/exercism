def find_anagrams(word, candidates):
    main_set, res = set(list(word.lower())), []

    for item in candidates:
        if item.lower() != word.lower() and len(word) == len(item):
            if set(list(item.lower())) & main_set == main_set:
                w = list(word.lower())

                for letter in list(item.lower()):
                    if w.count(letter) > 0:
                        w.pop(w.index(letter))

                if len(w) == 0:
                    res.append(item)

    return res
