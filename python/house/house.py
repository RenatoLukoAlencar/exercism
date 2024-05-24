def recite(start_verse, end_verse):
    splitter = " that "
    poem = "is the horse and the hound and the horn that belonged to the farmer sowing his corn that kept the rooster that crowed in the morn that woke the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.".split(
        splitter
    )
    res = splitter.join(poem[-(start_verse + 1) :])
    test = " ".join(poem[-start_verse].split(" ")[2:])
    sub = res.split(" ")[2] if res.split(" ")[2] != "the" else ""
    return [f"This is the {sub} {' '.join(res.split(' ')[3:])}".replace("  ", " ")]
