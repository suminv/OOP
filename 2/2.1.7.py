class Line:
    def __init__(self, x1, y1, x2, y2):
        """При этом в объекте line должны создаваться следующие приватные локальные свойства"""
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def set_coords(self, x1, y1, x2, y2):
        """Для изменения координат линии"""
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_coords(self):
        """Для получения кортежа из текущих координат линии."""
        return self.__x1, self.__y1, self.__x2, self.__y2

    def draw(self):
        """Для отображения в консоли списка текущих координат линии (в одну строчку через пробел)."""
        print(self.__x1, self.__y1, self.__x2, self.__y2)



line = Line(1, 2, 3, 4)
line.draw()
