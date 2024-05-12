from locomotive_engineer import fix_wagon_depot

expect = [
    [(2, "red"), (5, "blue"), (3, "orange")],
    [(4, "red"), (9, "blue"), (7, "orange")],
    [(8, "red"), (13, "blue"), (11, "orange")],
]

test = fix_wagon_depot(
    [
        ((2, "red"), (4, "red"), (8, "red")),
        ((5, "blue"), (9, "blue"), (13, "blue")),
        ((3, "orange"), (7, "orange"), (11, "orange")),
    ]
)

newArr = []
for key, i in enumerate(test):
    newArr.append(list(i))

print(f"test: {test}")
print(f"tet2: {newArr}")
print(f"expc: {expect}")
