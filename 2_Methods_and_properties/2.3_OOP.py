# Объекто-ориентированное программирование

class Point:
    list_of_points = []

    def __init__(self, x=0, y=0):
        self.move_to(x, y)
        Point.list_of_points.append(self)

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def go_home(self):
        self.move_to(0, 0)

    def print_point(self):
        print(f"Point with coordinates: ({self.x}, {self.y})")

    def get_distance(self, other_point):
        if not isinstance(other_point, Point):
            raise ValueError('Error! Second parameter must be a Point object')

        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5

    @staticmethod
    def get_list_of_points():
        return Point.list_of_points


point_1 = Point(3, 4)
point_1.print_point()
point_1.go_home()
point_1.print_point()

point_2 = Point(5, 12)
print(point_1.get_distance(point_2))

print(Point.get_list_of_points())


# Homework 1

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


dog_jack = Dog("Jack", 4)
print(dog_jack.description())
print(dog_jack.speak("Woof Woof"))
print(dog_jack.speak("Bow Wow"))


# Homework 2

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")

        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None

        return self.stack[-1]

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.stack)


s = Stack()
s.peek()
print(s.is_empty())
s.push('Cat')
s.push('Dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.is_empty())
s.push(777)
print(s.pop())
print(s.pop())
print(s.size())
