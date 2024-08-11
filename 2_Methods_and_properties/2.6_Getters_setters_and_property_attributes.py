# Геттеры, сеттеры и @property аттрибуты


# Пример 1: класс с публичными аттрибутами
class BankAccount:
    def __init__(self, name, balance):
        # Пример публичных аттрибутов
        self.name = name
        self.balance = balance


print("\nПример 1: класс с публичными аттрибутами")

account = BankAccount("John", 10000)

# Проблема 1: у нас есть доступ к аттрибутам
print(account.name)
print(account.balance)

# Проблема 2: можно установить значение аттрибута balance даже "hello"
account.balance = "hello"
print(account.balance)


# Пример 2: класс с приватным аттрибутом "balance" и геттерами/сеттерами для получения и изменения его
# Геттер и сеттер являются чем-то вроде middleware
class BankAccount2:
    def __init__(self, name, balance):
        # Пример публичных аттрибутов
        self.name = name
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, new_balance):
        # Проверка на тип данных
        if not isinstance(new_balance, (int, float)):
            raise ValueError("Balance must be a number")

        self.__balance = new_balance


print("\nПример 2: класс с приватным аттрибутом \"balance\" и геттерами/сеттерами для получения и изменения его")

account2 = BankAccount2("John", 10000)

# Теперь мы не можем получить значение баланса на прямую - можем только используя метод get_balance
print(account2.name)
print(account2.get_balance())

account2.set_balance(100)
print(account2.get_balance())


# Пример 3: класс с приватным аттрибутом "balance" и встроенной функцией property
# для получения и изменения его используя геттер и сеттер
class BankAccount3:
    def __init__(self, name, balance):
        # Пример публичных аттрибутов
        self.name = name
        self.__balance = balance

    def get_balance(self):
        print("Getting balance")
        return self.__balance

    def set_balance(self, new_balance):
        print("Setting balance")
        # Проверка на тип данных
        if not isinstance(new_balance, (int, float)):
            raise ValueError("Balance must be a number")

        self.__balance = new_balance

    def del_balance(self):
        print("Deleting balance")
        del self.__balance

    balance = property(fget=get_balance, fset=set_balance, fdel=del_balance)


print("\nПример 3: класс с приватным аттрибутом \"balance\" и встроенной функцией property\n"
      "для получения и изменения его используя геттер и сеттер")

account3 = BankAccount3("John", 10000)

# Теперь мы не можем получить значение баланса на прямую - можем только используя метод get_balance
print(account3.name)
print(account3.balance)  # Getting balance

account3.balance = 100  # Setting balance
print(account3.balance)
del account3.balance  # Deleting balance


# Homework
class UserMail:
    def __init__(self, login, email):
        self.login = login
        self.__email = email

    def get_email(self):
        return self.__email

    def set_email(self, value):
        if isinstance(value, str) and value.count("@") == 1 and value.find(".") > value.find("@"):
            self.__email = value
        else:
            print(f"ErrorMail: {value}")

    email = property(fget=get_email, fset=set_email)


print("\nHomework")

k = UserMail("k", "k@mail.com")
print(k.email)
k.email = [1, 2, 3]
k.email = "k@mail"
k.email = "k@mail@.com"
k.email = "new_k@mail.com"
print(k.email)
