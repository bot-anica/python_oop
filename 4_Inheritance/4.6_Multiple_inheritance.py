# ? Множественное наследование


class Doctor:
    def __init__(self, rank):
        self.rank = rank

    def graduate(self):
        print("Ура, я отучился на доктора!")

    def can_build(self):
        print("Я доктор, я умею строить")


class Builder:
    def __init__(self, degree):
        self.degree = degree

    def graduate(self):
        print("Ура, я отучился на строителя!")

    def can_build(self):
        print("Я строитель, я умею строить")


class Person(Doctor, Builder):
    def __init__(self, rank, degree):
        Doctor.__init__(self, rank)
        Builder.__init__(self, degree)

    def graduate(self):
        print("Посмотрим кем я стал")
        Doctor.graduate(self)
        Builder.graduate(self)

    def __str__(self):
        return f"Person has {self.rank} rank and {self.degree} degree"


person = Person(5, 'specialist')

person.can_build()
person.graduate()
print(Person.__mro__)  # Method resolution order (порядок поиска методов)
print(person)
