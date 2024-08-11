# ? Слоты, @property и наследование

# * Slots and @property
class Rectangle:
    __slots__ = '__width', 'height'

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value


# * Наследование

# * При наследовании дети не имеют ограничения __slots__
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)


square = Square(10)
square.color = 'green'
print(square.__dict__)


# * Чтобы вернуть ограничение, нужно явно указать __slots__
class Square2(Rectangle):
    __slots__ = 'color'  # __slots__ дочернего класса расширяет __slots__ родительского

    def __init__(self, length, color):
        super().__init__(length, length)
        self.color = color


square2 = Square2(10, 'red')
square2.color = 'green'
print(square2.__dict__)
