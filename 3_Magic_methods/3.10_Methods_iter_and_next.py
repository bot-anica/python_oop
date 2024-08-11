# Методы __iter__ и __next__

# __iter__ - итератор объекта
# __next__ - следующее значение итератора


class Mark:
    def __init__(self, marks):
        self.marks = marks
        self.index = 0

    def __iter__(self):
        print("Call __iter__")

        return self

    def __next__(self):
        print("Call __next__ Mark")

        if self.index >= len(self.marks):
            self.index = 0
            raise StopIteration("End of iteration")

        letter = self.marks[self.index]
        self.index += 1
        return letter


class Student:
    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks

    def __getitem__(self, item):
        return self.surname[item]

    def __iter__(self):
        print("Call __iter__")
        self.index = 0
        return iter(self.marks)

    def __next__(self):
        print("Call __next__ Student")

        if self.index >= len(self.name):
            self.index = 0
            raise StopIteration("End of iteration")

        letter = self.name[self.index]
        self.index += 1
        return letter


student_marks = Mark([5, 4, 3, 4, 5])
student = Student("Igor", "Sidorov", student_marks)

for i in student:
    print(i)


# Homework 1

class PowerTwo:
    def __init__(self, number):
        self.number = number

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if isinstance(value, int) and value >= 0:
            self.__number = value
        else:
            print("Error number")

    def __iter__(self):
        print("Call __iter__")
        self.index = 0
        return self

    def __next__(self):
        print("Call __next__ PowerTwo")

        if self.index > self.number:
            self.index = 0
            raise StopIteration("End of iteration")

        result = 2 ** self.index
        self.index += 1
        return result


print("\nHomework 1")

powerTwo = PowerTwo(3)
iterator = iter(powerTwo)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


# Homework 2

class InfinityIterator:
    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        result = self.index * 10
        self.index += 1
        return result


print("\nHomework 2")

iterator = iter(InfinityIterator())
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
