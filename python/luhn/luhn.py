class Luhn:
    """Class to represent an identification number checker."""
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        """Checks number validity as per the Luhn formula."""
        number = self.card_num.replace(' ', '')
        if len(number) > 1 and number.isdigit():
            return sum(self._parsed(number)) % 10 == 0
        return False     

    def _parsed(self, number):
        """Parses number's digits in reverse order."""
        result = []
        for idx, char in enumerate(reversed(number)):
            digit = int(char)
            if idx % 2 == 0:
                result.append(digit)
                continue
            digit += digit
            if digit < 9:
                result.append(digit)
                continue
            result.append(digit - 9)
        return result
