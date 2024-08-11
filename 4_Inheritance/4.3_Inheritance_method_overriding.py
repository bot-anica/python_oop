# ? Переопределение методов в дочерних классах

class Person:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print("Человек идёт")

    def talk(self):
        print("Человек говорит")

    def sleep(self):
        print("Человек спит")

    def combo(self):
        self.walk()
        self.talk()
        self.sleep()

    def __str__(self):
        return f"Person {self.name}"


class Doctor(Person):
    # Переопределяем метод walk
    def walk(self):
        print("Доктор идёт")

    def __str__(self):
        return f"Doctor {self.name}"


doctor = Doctor("Kate")
person = Person("Alex")

# doctor.walk()
# person.walk()
#
# doctor.talk()
# person.talk()
#
# print(doctor.name)
# print(person.name)
#
# print(doctor)
# print(person)

doctor.combo()
person.combo()
