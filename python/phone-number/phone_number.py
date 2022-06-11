from string import ascii_letters, punctuation


INVALID_NUMS = {"0": "zero", "1": "one"}
INVALID_PUNC = set(punctuation).difference("+", ".", "(", "-", ")")
VALIDATION = {
    "punctuation": "punctuations not permitted",
    "letters": "letters not permitted",
    "long": "more than 11 digits",
    "short": "incorrect number of digits",
    "country": "11 digits must start with 1",
    "area": "area code cannot start with",
    "exchange": "exchange code cannot start with",
}


class PhoneNumber:
    def __init__(self, phone_number):
        self.number = self._clean_number(phone_number)
        self.area_code = self.number[:3]
        self.exchange_code = self.number[3:6]
        self.subscriber = self.number[6:]

    def pretty(self):
        return f"({self.area_code})-{self.exchange_code}-{self.subscriber}"

    def _clean_number(self, phone_number):
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
        unique_chars = set(phone_number)

        if unique_chars.intersection(INVALID_PUNC):
            raise ValueError(VALIDATION["punctuation"])

        if unique_chars.intersection(ascii_letters):
            raise ValueError(VALIDATION["letters"])

    def _validate_length(self, length):
        if length > 11:
            raise ValueError(VALIDATION["long"])

        if length < 10:
            raise ValueError(VALIDATION["short"])

    def _validate_country(self, stripped):
        if not stripped.startswith("1"):
            raise ValueError(VALIDATION["country"])

    def _validate_codes(self, stripped):
        first, _, _, fourth = stripped[:4]

        if first in INVALID_NUMS:
            raise ValueError(f"{VALIDATION['area']} {INVALID_NUMS[first]}")

        if fourth in INVALID_NUMS:
            raise ValueError(f"{VALIDATION['exchange']} {INVALID_NUMS[fourth]}")
