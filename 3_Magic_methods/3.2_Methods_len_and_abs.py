# Методы __len__ и __abs__

# __len__ - длина итерируемого объекта
# __abs__ - абсолютное значение


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __len__(self):
        return len(self.name) + len(self.surname)

    def __abs__(self):
        return abs(len(self.name)) + abs(len(self.surname))


person = Person("John", "Doe")
print(len(person))


class Segment:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def __len__(self):
        return abs(self)

    def __abs__(self):
        return abs(self.point2 - self.point1)


segment = Segment(15, 9)
print(len(segment))
print(abs(segment))

segment = Segment(5, 9)
print(len(segment))
print(abs(segment))
