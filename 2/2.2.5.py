class WindowDlg:
    def __init__(self, title, width, height):
        """Создаем приватные локальные атрибуты"""
        self.__title = title
        self.__width = self.__height = None
        """Реализовать два объекта-свойства"""
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) == int and 0 <= value <= 1000:
            if self.__width:
                self.show()
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) == int and 0 <= value <= 1000:
            if self.__height:
                self.show()
            self.__height = value


    def show(self):
        print(f'{self.__title}: {self.__width}, {self.__height}')
