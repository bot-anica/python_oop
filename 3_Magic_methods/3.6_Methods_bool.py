# ? Метод __bool__

# __bool__ - преобразование в булево значение

# bool(class_instance)
# * Если метод __bool__ не реализован, то Python будет искать метод __len__
# * Если метод __len__ не реализован, то Python будет всегда возвращать True

class Point1:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = Point1(1, 2)
print(bool(p1))  # True

p2 = Point1(0, 0)
print(bool(p2))  # True


class Point2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        return abs(self.x - self.y)


p3 = Point2(1, 2)
print(bool(p3))  # True

p4 = Point2(9, 9)
print(bool(p4))  # False


class Point3:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __bool__(self):
        return self.x != 0 or self.y != 0


p5 = Point3(1, 2)
print(bool(p5))  # True

p6 = Point3(0, 0)
print(bool(p6))  # False


# Homework 1

class City:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        formated_name = value.lower().title()

        self.__name = formated_name

    def __str__(self):
        return self.name

    def __bool__(self):
        vowel_letters = ["a", "e", "i", "o", "u"]
        return not (self.name[-1] in vowel_letters)


p1 = City('new york')
print(p1)
print(bool(p1))

p2 = City('SaN fRaNCISco')
print(p2)
print(bool(p2))


class Quadrilateral:
    def __init__(self, width, height=None):
        self.width = width

        if height:
            self.height = height
        else:
            self.height = width

    def __str__(self):
        if self.width == self.height:
            return f"Квадрат со стороной {self.width}"
        else:
            return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __bool__(self):
        return self.width == self.height


q1 = Quadrilateral(5)
print(q1)
print(bool(q1))

q2 = Quadrilateral(5, 10)
print(q2)
print(bool(q2))
