# Инициализация объекта с помощью метода __init__

# Homework 1

class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = brand + " " + model


hp = Laptop("HP", "Pavillion 15", 1000)
lenovo = Laptop("Lenovo", "IdeaPad 330", 800)

print(hp.__dict__)
print(lenovo.__dict__)


# Homework 2

class SoccerPlayer:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.goals = 0
        self.assists = 0

    def score(self, goals=1):
        self.goals += goals

    def make_assist(self, assists=1):
        self.assists += assists

    def statistics(self):
        print(f"{self.name} {self.surname} - goals: {self.goals}, assists: {self.assists}")


john = SoccerPlayer("John", "Doe")
john.score(5)
john.make_assist(2)
john.statistics()  # John Doe - goals: 5, assists: 2

maria = SoccerPlayer("Maria", "Smith")
maria.score()
maria.statistics()  # Maria Smith - goals: 1, assists: 0


# Homework 3

class Zebra:
    def __init__(self):
        self.color = "white"

    def change_color(self):
        if self.color == "white":
            self.color = "black"
        else:
            self.color = "white"

    def which_stripe(self):
        print(f"{self.color.title()} stripe")
        self.change_color()


zebra = Zebra()
zebra.which_stripe()
zebra.which_stripe()
zebra.which_stripe()

zebra_1 = Zebra()
zebra_1.which_stripe()


# Homework 4
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        print(f"{self.first_name} {self.last_name}")

    def is_adult(self):
        return self.age >= 18


person = Person("John", "Doe", 25)
person.full_name()
print(person.is_adult())
