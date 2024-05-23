def find_anagrams(word, candidates):
    res, sword = [], word.casefold()
    for cand in candidates:
        if sword != cand.casefold() and sorted(sword) == sorted(cand.casefold()):
            res.append(cand)

    return res
