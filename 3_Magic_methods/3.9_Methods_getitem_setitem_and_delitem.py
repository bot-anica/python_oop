# ? Методы __getitem__, __setitem__ и __delitem__


# __getitem__ - получение элемента по индексу
# __setitem__ - изменение элемента по индексу
# __delitem__ - удаление элемента по индексу


class Vector:
    def __init__(self, *args):
        self.values = list(args)

    def __getitem__(self, item):
        return self.values[item]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __delitem__(self, key):
        del self.values[key]

    def __repr__(self):
        return str(self.values)


v1 = Vector(1, 2, 3, 4, 5, 6)
print(v1)

v1[0] = 10
print(v1)

del v1[0]
print(v1)


# Homework

class Building:
    def __init__(self, floors_quantity):
        self.floors_quantity = floors_quantity
        self.floors = [None] * floors_quantity

    def __setitem__(self, floor, company):
        self.floors[floor] = company

    def __getitem__(self, floor):
        return self.floors[floor]

    def __delitem__(self, floor):
        self.floors[floor] = None

    def __repr__(self):
        return str(self.floors)


b = Building(5)
b[0] = "Apple"
b[1] = "Samsung"
b[2] = "Xiaomi"
b[3] = "Huawei"
b[4] = "Nokia"

print(b)
print(b[2])
del b[2]
print(b)
