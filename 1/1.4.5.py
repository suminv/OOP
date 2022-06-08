"""
Подвиг 5. Объявите класс TriangleChecker, объекты которого можно было бы создавать командой:

tr = TriangleChecker(a, b, c)
Здесь a, b, c - длины сторон треугольника.

В классе TriangleChecker необходимо объявить метод is_triangle(), который бы возвращал, следующие коды:

1 - если хотя бы одна сторона не число или хотя бы одно число меньше или равно нулю;
2 - указанные числа a, b, c не могут являться длинами сторон треугольника;
3 - стороны a, b, c образуют треугольник.

Проверку параметров a, b, c проводить именно в таком порядке.

Прочитайте из входного потока строку, содержащую три числа, разделенных пробелами, командой:

a, b, c = map(int, input().split())
Затем, создайте объект tr класса TriangleChecker и передайте ему прочитанные значения a, b, c.
Вызовите метод is_triangle() из объекта tr и выведите результат на экран (код, который она вернет).


"""
class TriangleChecker:

    def __init__(self, a: int, b: int, c: int) -> None:
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self) -> int:
        if not isinstance(self.a, int) or \
                not isinstance(self.b, int) or \
                not isinstance(self.c, int) or \
                self.a <= 0 or self.b <= 0 or self.c <= 0:
            return 1
        elif self.a + self.b <= self.c or self.a + self.c <= self.b or self.c + self.b <= self.a:
            return 2
        else:
            return 3


a, b, c = map(int, input().split()) # эту строчку не менять

tr = TriangleChecker(a, b, c)

print(tr.is_triangle())

