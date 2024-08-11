# ? Делегирование

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def walk(self):
        print("Человек идёт")


class Doctor(Person):
    def __init__(self, name, surname, age):
        super().__init__(name, surname)
        self.age = age

    def walk(self):
        super().walk()  # вызов метода walk из родительского класс
        print(f"Доктор {self.name} {self.surname} идёт")


doctor = Doctor("Kate", "Ivanova", 25)
doctor.walk()


# ? Homework 1

class Transport:
    def __init__(self, brand, max_speed, kind=None):
        self.brand = brand
        self.max_speed = max_speed
        self.kind = kind

    def __str__(self):
        return f"Тип транспорта {self.kind} марки {self.brand} может развивать скорость {self.max_speed} км/час"


class Car(Transport):
    def __init__(self, brand, max_speed, mileage, gasoline_residue):
        super().__init__(brand, max_speed, "Car")
        self.mileage = mileage
        self.__gasoline_residue = 0
        self.gasoline_residue = gasoline_residue

    @property
    def gasoline_residue(self):
        return f"Осталось бензина {self.__gasoline_residue} литров"

    @gasoline_residue.setter
    def gasoline_residue(self, value):
        if not isinstance(value, int) or value < 0:
            print("Ошибка заправки автомобиля")
            return

        self.__gasoline_residue += value
        print(f"Объём топлива увеличен на {value} литров и составляет {self.__gasoline_residue} литров")


class Boat(Transport):
    def __init__(self, brand, max_speed, owners_name):
        super().__init__(brand, max_speed, "Boat")
        self.owners_name = owners_name

    def __str__(self):
        return f"Этой лодкой марки {self.brand} владеет {self.owners_name}"


class Plane(Transport):
    def __init__(self, brand, max_speed, capacity):
        super().__init__(brand, max_speed, "Plane")
        self.capacity = capacity

    def __str__(self):
        return f"Самолёт марки {self.brand} вмещает в себя {self.capacity} пассажиров"


print("\nHomework 1")

transport = Transport("Telega", 10)
print(transport)

bike = Transport("shkolnik", 20, "bike")
print(bike)

first_plane = Plane("Virgin Atlantic", 700, 450)
print(first_plane)

first_car = Car("BMW", 230, 75000, 300)
print(first_car)
print(first_car.gasoline_residue)
first_car.gasoline_residue = 20
print(first_car.gasoline_residue)

second_car = Car("Audi", 230, 70000, 130)
second_car.gasoline_residue = [None]


first_boat = Boat("Yamaha", 40, "Alex")
print(first_boat)


# ? Homework 2

class Initialization:
    def __init__(self, capacity, food):
        if not isinstance(capacity, int) or capacity < 0:
            print("Количество людей должно быть целым числом")
        else:
            self.capacity = capacity
            self.food = food


class Vegetarian(Initialization):
    def __init__(self, capacity, food):
        super().__init__(capacity, food)

    def __str__(self):
        return f"{self.capacity} людей предпочитают не есть мясо! Они предпочитают {self.food}"


class MeatEater(Initialization):
    def __init__(self, capacity, food):
        super().__init__(capacity, food)

    def __str__(self):
        return f"{self.capacity} людей предпочитают есть мясо! Помимо мясо они едят ещё и {self.food}"


class SweetTooth(Initialization):
    def __init__(self, capacity, food):
        super().__init__(capacity, food)

    def __str__(self):
        return f"{self.capacity} людей сладкоежек! Их самая любимая еда: {self.food}"

    def __eq__(self, other):
        if isinstance(other, int):
            return self.capacity == other
        elif isinstance(other, (MeatEater, Vegetarian)):
            return self.capacity == other.capacity

        print(f"Невозможно сравнить количество сладкоежек с {other}")
        return False

    def __lt__(self, other):
        if isinstance(other, int):
            return self.capacity < other
        elif isinstance(other, (MeatEater, Vegetarian)):
            return self.capacity < other.capacity

        print(f"Невозможно сравнить количество сладкоежек с {other}")
        return False

    def __gt__(self, other):
        if isinstance(other, int):
            return self.capacity > other
        elif isinstance(other, Initialization):
            return self.capacity > other.capacity

        print(f"Невозможно сравнить количество сладкоежек с {other}")
        return False


print("\nHomework 2")

vegetarian_first = Vegetarian(10000, ["Огурцы", "Баклажаны", "Помидоры"])
print(vegetarian_first)

vegetarian_second = Vegetarian([23], ["Картофель", "Огурцы", "Баклажаны", "Помидоры"])

meat_eater_first = MeatEater(15000, ["Жаренная картошка", "Рыба"])
print(meat_eater_first)

sweet_tooth_first = SweetTooth(30000, ["Мороженное", "Чипсы", "Шоколад"])
print(sweet_tooth_first)
print(sweet_tooth_first > vegetarian_first)
print(30000 == sweet_tooth_first)
print(sweet_tooth_first == 25000)
print(100000 < sweet_tooth_first)
print(100 < sweet_tooth_first)
print(100 < sweet_tooth_first < 20000)
print(100 < sweet_tooth_first < 100000)
