# ? Распространение исключений

def third_function():
    print("start second function")
    print(1 / 0)
    print("finish second function")


def second_function():
    print("start second function")
    third_function()
    print("finish second function")


def first_function():
    print("start first function")
    try:
        second_function()
    except ZeroDivisionError:
        print("Handled ZeroDivisionError in first function")
    print("finish first function")


print("HELLO")

first_function()
