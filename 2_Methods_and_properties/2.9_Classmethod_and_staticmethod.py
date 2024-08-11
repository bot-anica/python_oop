# Classmethod and staticmethod

class Example:
    def hello():
        print("Hello")

    def instance_hello(self):
        print("Instance hello", self)

    @staticmethod
    def static_hello():
        print("Static hello")

    @classmethod
    def class_hello(cls):
        print("Class hello", cls)


a = Example()

Example.hello()  # Hello
# a.hello()  # TypeError: Example.hello() takes 0 positional arguments but 1 was given

# Example.instance_hello()  # TypeError: Example.instance_hello() missing 1 required positional argument: 'self'
a.instance_hello()  # Instance hello

Example.static_hello()  # Static hello
a.static_hello()  # Static hello

Example.class_hello()  # Class hello (get Example class as first param)
a.class_hello()  # Class hello (get Example class as first param)


# Homework 1

class Robot:
    population = 0

    def __init__(self, name):
        self.name = name

    @staticmethod
    def increment_population():
        Robot.population += 1

    @staticmethod
    def decrement_population():
        Robot.population -= 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Robot.increment_population()
        self.__name = value
        print(f"Robot {self.name} was created")

    def destroy(self):
        Robot.decrement_population()
        print(f"Robot {self.name} was destroyed")

    def say_hello(self):
        print(f"Robot {self.name} says Hello!")

    @classmethod
    def how_many(cls):
        print(f"We have {cls.population} robots")


print("\nHomework 1")
r2 = Robot("R2-D2")
r2.say_hello()
Robot.how_many()
r2.destroy()
Robot.how_many()
