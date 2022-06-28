BRACKETS = {"{": "}", "[": "]", "(": ")"}
OPENING = set(BRACKETS)
CLOSING = set(BRACKETS.values())


def is_paired(input_string):
    """Verify that bracket pairs are matched and nested correctly."""
    
    unpaired = []
    
    for char in input_string:

        if char in OPENING:
           unpaired.append(char)
        elif char in CLOSING:
            if not unpaired or BRACKETS[unpaired.pop()] != char:
                return False

    return not unpaired
