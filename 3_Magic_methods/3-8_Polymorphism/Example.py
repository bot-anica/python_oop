from Lesson_3_8_Polymorphism import Rectangle, Square, Circle

rect1 = Rectangle(3, 4)
rect2 = Rectangle(12, 5)

sq1 = Square(5)
sq2 = Square(7)

c1 = Circle(5)
c2 = Circle(7)

figures = [rect1, rect2, sq1, sq2, c1, c2]

for figure in figures:
    print(figure, ": ", figure.get_area())
