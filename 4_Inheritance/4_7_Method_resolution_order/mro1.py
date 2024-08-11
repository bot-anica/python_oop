# ? Порядок вызова методов

class A:
    # pass
    def hello(self):
        print("Hello from A")


class B:
    pass
    # def hello(self):
    #     print("Hello from B")


class C(A, B):
    pass
    # def hello(self):
    #     print("Hello from C")


C().hello()
