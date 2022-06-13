from string import ascii_letters, punctuation


INVALID_NUMBERS = {"0": "zero", "1": "one"}
INVALID_PUNCTUATION = set(punctuation) - set("+.()-")
INVALID_LETTERS = set(ascii_letters)
VALIDATION = {
    "punctuation": "punctuations not permitted",
    "letters": "letters not permitted",
    "long": "more than 11 digits",
    "short": "incorrect number of digits",
    "country": "11 digits must start with 1",
    "code": "code cannot start with",
}


class PhoneNumber:
    """Class to validate and format American phone numbers."""

    def __init__(self, phone_number):
        self.number = self._clean_number(phone_number)
        self.area_code = self.number[:3]
        self.exchange_code = self.number[3:6]
        self.subscriber = self.number[6:]

    def pretty(self):
        """Return formatted phone number."""
        return f"({self.area_code})-{self.exchange_code}-{self.subscriber}"

    def _clean_number(self, phone_number):
        # Return cleaned number if it's valid
        self._validate_chars(phone_number)
        stripped = "".join(x for x in phone_number if x.isdigit())
        length = len(stripped)
        self._validate_length(length)

        if length == 11:
            self._validate_country(stripped)
            stripped = stripped[1:]

        self._validate_codes(stripped)

        return stripped

    def _validate_chars(self, phone_number):
        # Raise error if phone number contains letters or invalid punctuation
        unique_chars = set(phone_number)

        if unique_chars & INVALID_PUNCTUATION:
            raise ValueError(VALIDATION["punctuation"])

        if unique_chars & INVALID_LETTERS:
            raise ValueError(VALIDATION["letters"])

    def _validate_length(self, length):
        # Raise error if phone number's length is invalid
        if length > 11:
            raise ValueError(VALIDATION["long"])

        if length < 10:
            raise ValueError(VALIDATION["short"])

    def _validate_country(self, stripped):
        # Raise error if phone number has invalid country code
        if not stripped.startswith("1"):
            raise ValueError(VALIDATION["country"])

    def _validate_codes(self, stripped):
        # Raise error if area or exchange code starts with invalid digit
        first, _, _, fourth = stripped[:4]

        for digit, code_type in ((first, "area"), (fourth, "exchange")):
            if digit in INVALID_NUMBERS:
                raise ValueError(
                    f"{code_type} {VALIDATION['code']} {INVALID_NUMBERS[digit]}"
                )
