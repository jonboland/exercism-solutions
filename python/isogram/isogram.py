def is_isogram(string):
    """Determine if word or phrase is isogram."""
    return not any(string.lower().count(c) > 1
               for c in string if c.isalpha())
