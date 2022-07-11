import string
import random


class EmailValidator:
    characters = string.ascii_letters + string.digits + '._@'
    email_char = string.ascii_letters + string.digits + '_'

    def __new__(cls, *args, **kwargs):
        """Запретить создание объектов этого класса: при создании экземпляров должно возвращаться значение None,"""
        return None

    @classmethod
    def check_email(cls, email):
        if not cls.__is_email_str(email):
            return False

        if not set(email) < set(cls.characters):
            return False

        s = email.split('@')

        if len(s) != 2:
            return False

        if len(s[0]) > 100 or len(s[1]) > 50:
            return False

        if '.' not in s[1]:
            return False
        if email.count('..') > 0:
            return False
        return True

    @classmethod
    def get_random_email(cls):
        n = random.randint(4, 20)
        length = len(cls.email_char) - 1
        return ''.join(cls.email_char[random.randint(0, length)] for i in range(n)) + '@gmail.com'

    @staticmethod
    def __is_email_str(email):
        """Также в классе нужно реализовать приватный статический метод класса
        для проверки типа переменной email, если строка, то возвращается значение True, иначе - False."""
        return isinstance(email, str)


assert EmailValidator.check_email("sc_lib@list.ru") is True
assert EmailValidator.check_email("sc_lib@list_ru") is False
