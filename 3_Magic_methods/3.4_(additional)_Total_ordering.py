from functools import total_ordering

# Чтобы реализовать все методы сравнения, можно использовать декоратор @total_ordering,
# Который позволяет сократить код, реализовав только методы __eq__ и __lt__


@total_ordering
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.x < other.x or self.y < other.y


p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(1, 3)

print(p1 == p2)
print(p1 != p3)

print(p1 < p2)
print(p1 <= p3)

print(p1 > p2)
print(p1 >= p3)
print(p1 >= p3)
