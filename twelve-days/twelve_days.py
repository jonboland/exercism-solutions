day = (
    "first", "second", "third",
    "fourth", "fifth", "sixth",
    "seventh", "eighth", "ninth",
    "tenth", "eleventh", "twelfth",
    )

end = (
    "a Partridge in a Pear Tree",
    "two Turtle Doves",
    "three French Hens",
    "four Calling Birds",
    "five Gold Rings",
    "six Geese-a-Laying",
    "seven Swans-a-Swimming",
    "eight Maids-a-Milking",
    "nine Ladies Dancing",
    "ten Lords-a-Leaping",
    "eleven Pipers Piping",
    "twelve Drummers Drumming",
    )


def recite(start_verse, end_verse):
    """Output the lyrics to 'The Twelve Days of Christmas'."""
    carol = []
    for verse_num in range(start_verse, end_verse+1):
        gifts = (f"{', '.join(end[verse_num-1:0:-1])}, and {end[0]}"
                 if verse_num-1 else end[0])           
        verse = (f"On the {day[verse_num-1]} day of Christmas "
                 f"my true love gave to me: {gifts}.")
        carol.append(verse)
    return carol
