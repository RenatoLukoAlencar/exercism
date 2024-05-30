"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one, list_two):
    a, sa = set(list_one), ",".join(str(x) for x in list_one)
    b, sb = set(list_two), ",".join(str(x) for x in list_two)

    if list_one == list_two:
        return EQUAL

    elif (not list_one and len(list_two) > 0) or ((sa in sb) and a.issubset(b)):
        return SUBLIST

    elif (len(list_one) > 0 and not list_two) or ((sb in sa) and a.issuperset(b)):
        return SUPERLIST

    else:
        return UNEQUAL
