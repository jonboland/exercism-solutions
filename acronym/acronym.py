from re import findall


def abbreviate(words):
    """Convert a phrase to its acronym."""
    rx = r"(?:\b|(?<=_))(?<!')[^_\W]"
    return "".join(findall(rx, words.upper()))


