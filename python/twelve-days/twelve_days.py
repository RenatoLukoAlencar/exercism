def recite(start_verse, end_verse):
    poem = [
            "twelve Drummers Drumming, ",
            "eleven Pipers Piping, ",
            "ten Lords-a-Leaping, ",
            "nine Ladies Dancing, ",
            "eight Maids-a-Milking, ",
            "seven Swans-a-Swimming, ",
            "six Geese-a-Laying, ",
            "five Gold Rings, ",
            "four Calling Birds, ",
            "three French Hens, ",
            "two Turtle Doves, and ",
            "a Partridge in a Pear Tree."
        ]
    
    th_day, res= ["On the _ day of Christmas my true love gave to me: ","first", "second", "third","fourth", "fifth","sixth","seventh","eighth", "ninth", "tenth", "eleventh","twelfth"], []

    for part in range(start_verse, end_verse + 1):
        frase = th_day[0].replace("_", th_day[part])

        for verse in range(part, 0, -1):
            frase += (poem[verse * (-1)])

        res.append(frase)
    return res       
