LETTERS = (
    (1, ('A','E','I','O','U','L','N','R','S','T')),
    (2, ('D','G')),
    (3, ('B','C','M','P')),
    (4, ('F','H','V','W','Y')),
    (5,  'K'),
    (8, ('J','X')),
    (10,('Q','Z')),
    )

TILES = {x:k for k,v in LETTERS for x in v}


def score(word):
    """Compute the scrabble score for a word."""
    return sum(TILES[x] for x in word.upper())
