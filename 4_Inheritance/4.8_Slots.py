# ? Слоты
from timeit import timeit


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class PointSlots:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


def make_cl1():
    point = Point(1, 2)
    point.x = 10
    point.x
    del point.x

def make_cl2():
    point_slots = PointSlots(1, 2)
    point_slots.x = 10
    point_slots.x
    del point_slots.x

print(timeit(make_cl1))
print(timeit(make_cl2))
