# Декоратор @property

# Класс с приватным аттрибутом "balance" и декоратором @property для получения, изменения и удаления его
class BankAccount4:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance  # здесь аттрибут __balance назначается используя setter (line 13)

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_balance):
        # Проверка на тип данных
        if not isinstance(new_balance, (int, float)):
            raise ValueError("Balance must be a number")

        self.__balance = new_balance

    @balance.deleter
    def balance(self):
        print("Deleting balance")
        del self.__balance


print("\nПример 4: класс с приватным аттрибутом \"balance\" и декоратором @property для получения и изменения его")

account4 = BankAccount4("John", 10000)

# Теперь мы не можем получить значение баланса на прямую - можем только используя метод get_balance
print(account4.name)
print(account4.balance)

account4.balance = 100
print(account4.balance)
del account4.balance


# Homework 1

class Notebook:
    def __init__(self, notes):
        self._notes = notes

    @property
    def notes_list(self):
        for index, note in enumerate(self._notes):
            print(f"{index + 1}. {note}")


print("\nHomework 1")
note = Notebook(["Buy milk", "Buy bread", "Buy shampoo", "Buy eggs"])
note.notes_list


# Homework 2

class Money:
    def __init__(self, dollars, cents):
        self._total_cents = dollars * 100 + cents

    @property
    def total_cents(self):
        return self._total_cents

    @property
    def dollars(self):
        return self.total_cents // 100

    @property
    def cents(self):
        return self.total_cents % 100

    @dollars.setter
    def dollars(self, value):
        if isinstance(value, int) and value >= 0:
            self._total_cents = value * 100 + self.cents
        else:
            print("Error dollars")

    @cents.setter
    def cents(self, value):
        if isinstance(value, int) and 0 <= value < 100:
            self._total_cents = self.dollars * 100 + value
        else:
            print("Error cents")

    def __str__(self):
        return f"Ваше состояние состовляет {self.dollars} долларов и {self.cents} центов"


Bill = Money(101, 99)
print(Bill)
print(Bill.dollars, Bill.cents)
print(Bill.total_cents)
Bill.dollars = '666'
Bill.dollars = -10
Bill.dollars = 666
print(Bill)
Bill.cents = '12'
Bill.cents = -12
Bill.cents = 12
print(Bill)

