# ? Принцип наследования

# * Наследование - это способность одного объекта наследовать все свойства и методы другого объекта

class Person:
    def can_walk(self):
        print("Я могу ходить")

    def can_talk(self):
        print("Я могу говорить")


class Doctor(Person):
    def can_cure(self):
        print("Я могу лечить")


class Ortoped(Doctor):
    pass


class Architect(Person):
    def can_build(self):
        print("Я могу строить")


doctor = Doctor()
print(issubclass(Doctor, Person))  # True
print(isinstance(doctor, Doctor))  # True
print(isinstance(doctor, Person))  # True
# doctor.can_cure()
# doctor.can_walk()
# doctor.can_talk()

architect = Architect()
print(issubclass(Architect, Person))  # True
print(isinstance(architect, Architect))  # True
print(isinstance(architect, Person))  # True
# architect.can_build()
# architect.can_walk()
# architect.can_talk()

ortoped = Ortoped()
print(issubclass(Ortoped, Person))  # True
print(isinstance(ortoped, Ortoped))  # True
print(isinstance(ortoped, Doctor))  # True
print(isinstance(ortoped, Person))  # True
# ortoped.can_cure()
# ortoped.can_walk()
# ortoped.can_talk()


# ? Homework

class Vehicle:
    pass


class Car(Vehicle):
    pass


class Plane(Vehicle):
    pass


class Boat(Vehicle):
    pass


class RaceCar(Car):
    pass
