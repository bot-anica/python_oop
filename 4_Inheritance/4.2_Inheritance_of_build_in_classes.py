# ? Наследование от встроенных классов

class MyList(list):
    pass


my_list = MyList()
my_list.append(1)
print(my_list)


# ? Homework

class NewInt(int):
    def repeat(self, quantity=2):
        return int(str(self) * quantity)

    def to_bin(self):
        return int(bin(self)[2:])


number_1 = NewInt(9)
print(number_1.repeat())

number_2 = NewInt(number_1 + 5)
print(number_2.repeat(3))

number_3 = NewInt(NewInt(7) * NewInt(5))
print(number_3.to_bin())
