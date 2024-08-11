# ? Полиморфизм

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def __str__(self):
        return f"Прямоугольник со сторонами {self.width} и {self.height}"


class Square():
    def __init__(self, width):
        self.width = width

    def get_area(self):
        return self.width ** 2

    def __str__(self):
        return f"Квадрат со стороной {self.width}"


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * (self.radius ** 2)

    def __str__(self):
        return f"Круг с радиусом {self.radius}"


# Homework

class UnitedKingdom:
    @staticmethod
    def capital():
        print("London is the capital of Great Britain")

    @staticmethod
    def language():
        print("English is the official language of Great Britain")


class Spain:
    @staticmethod
    def capital():
        print("Madrid is the capital of Spain")

    @staticmethod
    def language():
        print("Spanish is the official language of Spain")


britain = UnitedKingdom()
spain = Spain()

for country in (britain, spain):
    country.capital()
    country.language()
