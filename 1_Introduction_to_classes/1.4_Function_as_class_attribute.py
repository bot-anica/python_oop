# Функция как аттрибут КЛАССА

# Пример класса с аттрибутами
class Person:
    name = "John"
    age = 36

    def say_hello(self):
        print('Hello, my name is', self.name)

    def say_full_name(self):
        if hasattr(self, 'surname'):
            print('My full name is', self.name, self.surname)
        else:
            print('I have only first name', self.name)

    def set_surname(self, value):
        setattr(self, 'surname', value)


person = Person()
person.say_hello()
person.set_surname('Smith')
person.say_full_name()


# Homework 1

class Lion:
    def roar(self):
        print('Rrrrrrr!!!')


simba = Lion()
simba.roar()


# Homework 2

class Counter:
    def start_from(self, value=0):
        setattr(self, 'value', value)

    def increment(self):
        setattr(self, 'value', self.value + 1)

    def display(self):
        print(f"Текущее значение счётчика: {self.value}")

    def reset(self):
        setattr(self, 'value', 0)


first_counter = Counter()
first_counter.start_from(5)
first_counter.display()
first_counter.increment()
first_counter.display()
first_counter.reset()
first_counter.display()


# Homework 3

class Point:
    def set_coordinates(self, x, y):
        setattr(self, 'x', x)
        setattr(self, 'y', y)

    def get_distance(self, other_point):
        if isinstance(other_point, Point):
            return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5
        else:
            print('Error! Second parameter must be a Point object')


point_1 = Point()
point_1.set_coordinates(0, 0)

point_2 = Point()
point_2.set_coordinates(3, 4)

print(point_1.get_distance(point_2))
print(point_2.get_distance(10))
