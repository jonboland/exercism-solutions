INVALID = {"0", "1"}
VALIDATION = {
    "wrong length": "The number of digits is incorrect.",
    "invalid digit": "Area and exchange codes cannot start with 0 or 1.",
    "wrong code": "Eleven digit numbers must begin with 1.",
}


class PhoneNumber:
    def __init__(self, phone_number):
        self.number = self._clean_number(phone_number)
        self.area_code = self.number[:3]
        self.ex_code = self.number[3:6]
        self.sub_number = self.number[6:]

    def pretty(self):
        return f"({self.area_code})-{self.ex_code}-{self.sub_number}"

    def _clean_number(self, phone_number):
        stripped = [x for x in phone_number if x.isdigit()]
        length = len(stripped)
        self._validate(stripped, length)

        return "".join(stripped[1:] if length == 11 else stripped)

    def _validate(self, stripped, length):
        if length > 11 or length < 10:
            raise ValueError(VALIDATION["wrong length"])

        first, second, _, fourth, fifth = stripped[:5]

        if length == 10:
            if {first, fourth}.intersection(INVALID):
                raise ValueError(VALIDATION["invalid digit"])

        if length == 11:
            if first != "1":
                raise ValueError(VALIDATION["wrong code"])
            if {second, fifth}.intersection(INVALID):
                raise ValueError(VALIDATION["invalid digit"])
