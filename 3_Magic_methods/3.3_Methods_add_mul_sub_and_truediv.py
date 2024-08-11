# ? Методы __add__, __mul__, __sub__ и __truediv__


# __add__ - сложение
# __mul__ - умножение
# __sub__ - вычитание
# __truediv__ - деление


# __add__

class Vector:
    def __init__(self, *args):
        self.values = args

    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, value):
        filtered_values = []

        for item in value:
            if isinstance(item, int):
                filtered_values.append(item)

        self.__values = sorted(filtered_values)

    @staticmethod
    def sum(item_1, item_2):
        result = []

        if isinstance(item_2, int):
            result = [item_1.values[i] + item_2 for i in range(len(item_1.values))]
        elif isinstance(item_2, Vector):
            if len(item_1.values) != len(item_2.values):
                print("Списки должны иметь одинаковую длину!")
                return

            result = [item_1.values[i] + item_2.values[i] for i in range(len(item_1.values))]
        else:
            print(f"Вектор нельзя сложить с {item_2}")

        return result

    @staticmethod
    def mul(item_1, item_2):
        result = []

        if isinstance(item_2, int):
            result = [item_1.values[i] * item_2 for i in range(len(item_1.values))]
        elif isinstance(item_2, Vector):
            if len(item_1.values) != len(item_2.values):
                print("Списки должны иметь одинаковую длину!")
                return

            result = [item_1.values[i] * item_2.values[i] for i in range(len(item_1.values))]
        else:
            print(f"Вектор нельзя перемножить с {item_2}")

        return result

    @staticmethod
    def sub(item_1, item_2):
        result = []

        if isinstance(item_2, int):
            result = [item_1.values[i] - item_2 for i in range(len(item_1.values))]
        elif isinstance(item_2, Vector):
            if len(item_1.values) != len(item_2.values):
                print("Списки должны иметь одинаковую длину!")
                return

            result = [item_1.values[i] - item_2.values[i] for i in range(len(item_1.values))]
        else:
            print(f"Из вектора нельзя вычесть {item_2}")

        return result

    @staticmethod
    def truediv(item_1, item_2):
        result = []

        if isinstance(item_2, int):
            result = [item_1.values[i] // item_2 for i in range(len(item_1.values))]
        elif isinstance(item_2, Vector):
            if len(item_1.values) != len(item_2.values):
                print("Списки должны иметь одинаковую длину!")
                return

            result = [item_1.values[i] // item_2.values[i] for i in range(len(item_1.values))]
        else:
            print(f"Вектор нельзя разделить на {item_2}")

        return result

    def __add__(self, other):
        result = Vector.sum(self, other)
        return Vector(*result)

    def __mul__(self, other):
        result = Vector.mul(self, other)
        return Vector(*result)

    def __sub__(self, other):
        result = Vector.sub(self, other)
        return Vector(*result)

    def __truediv__(self, other):
        result = Vector.truediv(self, other)
        return Vector(*result)

    def __str__(self):
        if len(self.values) == 0:
            return "Пустой вектор"
        else:
            return f"Вектор({", ".join(map(str, self.values))})"


v1 = Vector(1, 2, 3)
print(v1)

v2 = Vector(3, 4, 5)
print(v2)

print("\nSum")
v3 = v1 + v2
print(v3)

v4 = v3 + 5
print(v4)

v5 = v4 + 'hi'
print(v5)

print("\nMul")
v6 = v1 * v2
print(v6)

v7 = v1 * 2
print(v7)

v8 = v1 * 'hi'
print(v8)

print("\nSub")
v9 = v1 - v2
print(v9)

v10 = v1 - 2
print(v10)

v11 = v1 - 'hi'
print(v11)

print("\nTruediv")
v12 = v1 / v2
print(v12)

v13 = v1 / 2
print(v13)

v14 = v1 / 'hi'
print(v14)
