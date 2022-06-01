"""
Необходимо перед классом StreamReader объявить еще один класс StreamData с методом:

def create(fields, lst_values): ...

который бы на входе получал список полей FIELDS (передается в атрибут fields) и список строк lst_in (передается в атрибут lst_values) и формировал бы в объекте класса StreamData локальные свойства с именами полей из fields и соответствующими значениями из lst_values.

Если создание локальных свойств проходит успешно, то метод create() возвращает True, иначе - False. Если число полей и число строк не совпадает, то метод create() возвращает False.

P.S. В программе нужно дополнительно объявить только класс StreamData. Больше ничего делать не нужно.


"""

import sys


class StreamData:
    def create(self, FIELDS, lst_in):
        if len(FIELDS) == len(lst_in):
            for i in range(len(lst_in)):
                setattr(self, FIELDS[i], lst_in[i])
            return True
        return False


class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        # lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        lst_in = [1, 2, 3]
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


sr = StreamReader()
data, result = sr.readlines()
print(data.__dict__)