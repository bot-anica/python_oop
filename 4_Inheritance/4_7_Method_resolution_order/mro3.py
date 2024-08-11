# ? Homework

class H:
    pass


class D(H):
    pass


class E(H):
    pass


class F(H):
    pass


class G(H):
    pass


class B(D, E):
    pass


class C(F, G):
    pass


class A(B, C):
    pass


# MRO: A -> B -> D -> E -> C -> F -> G -> H -> object

def get_mro(cls):
    print(*[c.__name__ for c in cls.mro()], sep=' -> ')


get_mro(A)
