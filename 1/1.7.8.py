import re
from string import ascii_lowercase, digits


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    def __init__(self, number, name):
        if self.check_card_number(number) and self.check_name(name):
            self.number = number
            self.mane = name


    @classmethod
    def check_card_number(cls, number):
        # return bool(re.fullmatch(r"\d{4}(?:-\d{4}){3}", number))
        number = number.split('-')
        for indx, value in enumerate(number):
            if len(value) == 4 and value.isdigit():
                return True
            else:
                return False

    @classmethod
    def check_name(cls, name):
        # return bool(re.fullmatch(r"[A-Z\d]+ [A-Z\d]+", name))
        if len(name.split()) != 2:
            return False
        return set(name.replace(' ', '')).issubset(cls.CHARS_FOR_NAME)


is_number = CardCheck.check_card_number("1234-5678-9012-0000")
is_name = CardCheck.check_name("SERGEI BALAKIREV")
print(is_number)
print(is_name)
