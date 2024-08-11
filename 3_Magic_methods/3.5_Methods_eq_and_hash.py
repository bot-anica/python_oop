# ? Методы __eq__ и __hash__

# __eq__ - сравнение
# __hash__ - хэш

# * При определении метода __eq__, слетает метод __hash__
# * Поэтому нам необходимо переопределить метод __hash__
# * Изначально методы __eq__ и __hash__ сравнивают объекты по id
# * Так как мы переопределили метод __eq__, то Python автоматически делает метод __hash__ неактивным
# * Поэтому нам нужно переопределить метод __hash__

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def __hash__(self):
        return hash((self.x, self.y))



p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(1, 3)

print(p1 == p2)
print(p1 == p3)

print(hash(p1))
print(hash(p2))
print(hash(p3))

# * В качестве ключей у Dict могут быть только хэшируемые объекты
# * Поэтому теперь мы можем использовать экземпляры класса Point в качестве ключей

r = {
    p2: "p2",
    p3: "p3",
}

print(r[p3])
