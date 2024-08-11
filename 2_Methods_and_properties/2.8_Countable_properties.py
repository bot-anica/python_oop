# Вычисляемые свойства

class Square:
    def __init__(self, side):
        self.side = side

    # Площадь (area) - это вычисляемое свойство, которое меняется в зависимости от размера квадрат
    @property
    def area(self):
        return self.side ** 2

print("\nПример 1: вычисляемое свойство")
a = Square(5)
print(a.area)


# Допустим, что размер квадрата не меняется, а площадь нам нужно использовать в нескольких местах
# Тогда площадь будет пересчитываться при каждом её запросе (a.area)

# Чтобы этого избежать мы будем запоминать его
class Square2:
    def __init__(self, side):
        self.side = side

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value):
        self.__side = value
        self.__area = None
        self.__perimeter = None

    # Площадь (area) - это вычисляемое свойство, которое меняется в зависимости от размера квадрат
    @property
    def area(self):
        if self.__area is None:
            print("Вычисляем площадь")
            self.__area = self.side ** 2

        return self.__area

    @property
    def perimeter(self):
        if self.__perimeter is None:
            print("Вычисляем периметр")
            self.__perimeter = self.side * 4

        return self.__perimeter


print("\nПример 2: вычисляемые свойства с запоминанием")
b = Square2(11)
print(b.area)
print(b.perimeter)
print(b.area)
print(b.perimeter)

b.side = 5
print(b.area)
print(b.perimeter)


# Homework 1

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.__area = None

    @property
    def length(self):
        return self.__length

    @property
    def width(self):
        return self.__width

    @length.setter
    def length(self, value):
        self.__length = value
        self.__area = None

    @width.setter
    def width(self, value):
        self.__width = value
        self.__area = None

    @property
    def area(self):
        if self.__area is None:
            self.__area = self.length * self.width
        return self.__area


print("\nHomework 1")
r1 = Rectangle(3, 5)
r2 = Rectangle(6, 1)

print(r1.area)
print(r2.area)

r1.width = 10
r2.length = 8
r2.width = 2

print(r1.area)
print(r2.area)


# Homework 2

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @property
    def day(self):
        return self.__day

    @property
    def month(self):
        return self.__month

    @property
    def year(self):
        return self.__year

    @day.setter
    def day(self, value):
        if isinstance(value, int) and 1 <= value <= 31:
            self.__day = value
        else:
            print("Error day")

    @month.setter
    def month(self, value):
        if isinstance(value, int) and 1 <= value <= 12:
            self.__month = value
        else:
            print("Error month")

    @year.setter
    def year(self, value):
        if isinstance(value, int) and 1 <= value <= 9999:
            self.__year = value
        else:
            print("Error year")

    @property
    def date(self):
        print("Date:")
        return f"{self.day:02}/{self.month:02}/{self.year:04}"

    @property
    def usa_date(self):
        print("USA date:")
        return f"{self.month:02}-{self.day:02}-{self.year:04}"


print("\nHomework 2")
d1 = Date(5, 10, 2001)
d2 = Date(15, 3, 999)

print(d1.date)
print(d1.usa_date)
print(d2.date)
print(d2.usa_date)
