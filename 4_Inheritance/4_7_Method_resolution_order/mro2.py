# * MRO - Method Resolution Order
# * MRO использует алгоритм С3-линеаризации

# 1. Каждый класс должен входить в список ровно 1 раз.
# 2. Если какой-то класс D наследуется от нескольких классов, допустим, A, B, C (class D(A, B, C):),
#    в таком же порядке они должны появиться в MRO. D -> ... -> A -> ... -> B -> ... -> C -> ...
#    Между ними могут оказаться и другие классы, но исходный порядок должен быть соблюден.
# 3. Родители данного класса должны появляться по порядку старшинства.
#    Сначала идут непосредственные родители, потом дедушки и бабушки, но не наоборот.

class O:
    def hello(self):
        print("Hello from O")


class A(O):
    pass


class B(O):
    pass


class C(O):
    pass


class D(O):
    pass


class E(O):
    def hello(self):
        print("Hello from E")


class K1(C, A, B):
    pass


class K2(A, D):
    pass


class K3(B, D, E):
    def hello(self):
        print("Hello from K3")


class Z(K1, K2, K3):
    pass


print(Z.mro())
print(Z.__mro__)


def get_mro(cls):
    print(*[c.__name__ for c in cls.mro()], sep=' -> ')


get_mro(Z)  # Z -> K1 -> C -> K2 -> A -> K3 -> B -> D -> E -> O -> object

# 1. Если на родительский класс ссылается только 1 класс, то указываем его.
# 2. Если на класс ссылается какой-то класс, который ещё не указан в MRO, то мы пропускаем его.
# 3. Если в MRO уже указаны все классы ссылающиеся на их общего родителя,
#    то после указания последнего из этих классов указывается их родитель.

Z().hello()

# Вызовется метод hello у класса K3, потому что в MRO он расположен раньше,
# чем другие классы, у которых есть такой же метод (E, O).
