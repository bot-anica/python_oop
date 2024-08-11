# ? Методы сравнения

# __eq__ - равенство (==)
# __ne__ - неравенство (!=)
# __lt__ - меньше (<)
# __le__ - меньше или равно (<=)
# __gt__ - больше (>)
# __ge__ - больше или равно (>=)


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area < other.area
        elif isinstance(other, int):
            return self.area < other

    def __le__(self, other):
        return self == other or self < other

    def __gt__(self, other):
        if isinstance(other, Rectangle):
            return self.area > other.area
        elif isinstance(other, int):
            return self.area > other


r1 = Rectangle(3, 5)
r2 = Rectangle(3, 5)
r3 = Rectangle(4, 5)

print(r1 == r2)
print(r1 == r3)
print(r1 != r3)
print(r1 <= r2)
print(r1 <= r3)
print(14 < r1)
print(16 > r3)
print(16 >= r1)


# Homework

class ChessPlayer:
    def __init__(self, name, surname, rating):
        self.name = name
        self.surname = surname
        self.rating = rating

    def __eq__(self, other):
        if isinstance(other, ChessPlayer):
            return self.rating == other.rating
        elif isinstance(other, int):
            return self.rating == other
        else:
            return "Невозможно выполнить сравнение"

    def __gt__(self, other):
        if isinstance(other, ChessPlayer):
            return self.rating > other.rating
        elif isinstance(other, int):
            return self.rating > other
        else:
            return "Невозможно выполнить сравнение"

    def __lt__(self, other):
        if isinstance(other, ChessPlayer):
            return self.rating < other.rating
        elif isinstance(other, int):
            return self.rating < other
        else:
            return "Невозможно выполнить сравнение"


print("\nHomework")

magnus = ChessPlayer("Carlsen", "Magnus", 2847)
ian = ChessPlayer("Ian", "Nepomniachtchi", 2789)

print(magnus == 4000)
print(ian == 2789)
print(magnus == ian)
print(magnus > ian)
print(magnus < ian)
print(magnus < [1, 2])
