# Публичные, защищенные и приватные аттрибуты и методы


# Пример класса с публичными аттрибутами
class BankAccount1:
    def __init__(self, name, balance, passport):
        # Пример публичных аттрибутов
        self.name = name
        self.balance = balance
        self.passport = passport

    def print_data(self):
        print(self.name, self.balance, self.passport)


account_1 = BankAccount1("John", 10000, 123456789)
account_1.print_data()

# Все наши данные публичные, их можно получить по имени
print(account_1.name)
print(account_1.balance)
print(account_1.passport)


# Пример класса с защищенными аттрибутами
# На самом деле защищённые аттрибуты имеют открытый доступ
# Их можно получить по имени
# Такие аттрибуты используют для согласования между разработчиками, что их лучше не использовать вне класса
class BankAccount2:
    def __init__(self, name, balance, passport):
        # Пример защищенных аттрибутов
        self._name = name
        self._balance = balance
        self._passport = passport

    def print__protected_data(self):
        print(self._name, self._balance, self._passport)


account_1 = BankAccount2("John", 10000, 123456789)
account_1.print__protected_data()

# Все наши данные публичные, их можно получить по имени
print(account_1._name)  # John
print(account_1._balance)  # 10000
print(account_1._passport)  # 123456789


# Пример класса с приватными аттрибутами (Инкапсуляция)
# Такие аттрибуты мы можем получить только изнутри класса
# (используя собственные методы класса предоставляющие доступ к приватным аттрибутам)
class BankAccount3:
    def __init__(self, name, balance, passport):
        # Пример защищенных аттрибутов
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    def print_private_data(self):
        print(self.__name, self.__balance, self.__passport)


account_1 = BankAccount3("John", 10000, 123456789)
account_1.print_private_data()

# Все наши данные публичные, их можно получить по имени
# print(account_1.__name)  # AttributeError: 'BankAccount3' object has no attribute '__name'
# print(account_1.__balance)  # AttributeError: 'BankAccount3' object has no attribute '__balance'
# print(account_1.__passport)  # AttributeError: 'BankAccount3' object has no attribute '__passport'


# Получение доступа к приватным аттрибутам и методам по имени
# Используя функцию dir(class_instance) мф можем получить список всех аттрибутов и методов класса
print(dir(account_1))  # '_BankAccount3__balance', '_BankAccount3__name', '_BankAccount3__passport' ...

# И теперь мы можем получить значения приватных аттрибутов или вызвать приватные методы как публичные
print(account_1._BankAccount3__balance)  # 10000
print(account_1._BankAccount3__name)  # John
print(account_1._BankAccount3__passport)  # 123456789


# Для полноценной защиты или скрытия аттрибутов и методов можно использовать библиотеку accessify
# Она имеет декораторы @protected и @private
# https://pypi.org/project/accessify/


# Homework 1

class Student:
    def __init__(self, name, age, branch):
        self.__name = name
        self.__age = age
        self.__branch = branch

    def __display_details(self):
        print(f"Name: {self.__name}\nAge: {self.__age}\nBranch: {self.__branch}")

    def access_private_method(self):
        self.__display_details()


obj = Student("John", 20, "CSE")
obj.access_private_method()


# Homework 2

class PizzaMaker:
    def __make_paperoni(self):
        pass

    def _make_barbeque(self):
        pass


print(PizzaMaker.__dict__.keys())

pizza_maker = PizzaMaker()
pizza_maker._make_barbeque()
pizza_maker._PizzaMaker__make_paperoni()
