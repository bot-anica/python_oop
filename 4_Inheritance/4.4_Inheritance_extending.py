# ? Расширение дочерних классов

# * Расширение дочерних классов - добавление новых методов в дочерний класс

class Person:
    def walk(self):
        print("Человек идёт")

    def combo(self):
        if hasattr(self, "sleep"):
            self.sleep()
        self.walk()
        if hasattr(self, "age"):
            print(self.age)

class Doctor(Person):
    age = 25

    def sleep(self):
        print("Доктор спит")

    def walk(self):
        print("Доктор идёт")


person = Person()
doctor = Doctor()

print('-' * 50)
person.walk()
doctor.walk()

print('-' * 50)
# person.sleep() - AttributeError: 'Person' object has no attribute 'sleep'
doctor.sleep()

print('-' * 50)
person.combo()
doctor.combo()
