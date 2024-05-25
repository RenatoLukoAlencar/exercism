def recite(start_verse, end_verse):
    poem = [
        "",
        "",
        "malt that lay in the ",
        "rat that ate the ",
        "cat that killed the ",
        "dog that worried the ",
        "cow with the crumpled horn that tossed the ",
        "maiden all forlorn that milked the ",
        "man all tattered and torn that kissed the ",
        "priest all shaven and shorn that married the ",
        "rooster that crowed in the morn that woke the ",
        "farmer sowing his corn that kept the ",
        "horse and the hound and the horn that belonged to the ",
    ]
    song = []
    for i in range(start_verse, end_verse + 1):
        verse = ""
        for j in range(i, 0, -1):
            verse += poem[j]

        song.append(f"This is the {verse}house that Jack built.")
    return song
