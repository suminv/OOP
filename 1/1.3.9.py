"""
Необходимо в класс DataBase:

class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')
добавить два метода:

insert(self, data) - для добавления в список lst_data новых данных из переданного списка строк data;
select(self, a, b) - для отбора и возврата записей в диапазоне [a; b] по их индексам из списка lst_data.

Каждая запись в списке lst_data должна быть представлена словарем в формате:

{'id': 'номер', 'name': 'имя', 'old': 'возраст', 'salary': 'зарплата'}

Например:

{'id': '1', 'name': 'Сергей', 'old': '35', 'salary': '120000'}

P. S. Ваша задача только добавить два метода в класс DataBase.

"""

import sys

# программу не менять, только добавить два метода
lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')


    def insert(self, data):
        for i in data:
            self.lst_data.append(dict(zip(self.FIELDS, i.split())))

    def select(self, a, b):
        return self.lst_data[a:b+1]



db = DataBase()
db.insert(lst_in)
