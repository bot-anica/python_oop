from enum import Enum


# Методы __str__ и __repr__

# __str__ - строковое представление объекта
# __repr__ - представление объекта в отладочном режиме


class Lion1:
    def __init__(self, name):
        self.name = name


lion_1 = Lion1("Alex")
print(lion_1)  # <__main__.Lion object at 0x101c0d160>
print(lion_1.__str__())  # <__main__.Lion object at 0x101c0d160>
print(lion_1.__repr__())  # <__main__.Lion object at 0x101c0d160>


# Используем методы __str__ и __repr__
class Lion2:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Lion({self.name})"


lion_2 = Lion2("Alex")
print(lion_2)  # Alex
print(lion_2.__str__())  # Alex
print(lion_2.__repr__())  # Lion(Alex)


# Homework 1

class Gender(Enum):
    MALE = "male"
    FEMALE = "female"


class Person:
    def __init__(self, name, surname, gender=Gender.MALE):
        self.name = name
        self.surname = surname
        self.gender = gender

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value: Gender = Gender.MALE):
        if value == Gender.MALE or value == Gender.FEMALE:
            self.__gender = value
        else:
            print("Не знаю что вы имели ввиду. Пусть это будет мужчина.")
            self.__gender = Gender.MALE

    def __str__(self):
        if self.gender == Gender.MALE:
            return f"Мужчина {self.name} {self.surname}"
        else:
            return f"Женщина {self.name} {self.surname}"


p1 = Person("Chuck", "Norris")
print(p1)
p2 = Person("Mila", "Kunis", Gender.FEMALE)
print(p2)
p3 = Person("Оби-Ван", "Кеноби", True)
print(p3)


# Homework 2

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

        self.__values = filtered_values

    def __str__(self):
        if len(self.values) == 0:
            return "Пустой вектор"
        else:
            return f"Вектор({", ".join(map(str, self.values))})"


v1 = Vector(1, 2, 3, 4, 5, 6)
print(v1)
v2 = Vector()
print(v2)
