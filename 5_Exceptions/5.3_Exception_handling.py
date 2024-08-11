# ? Обработка исключений

welcome_message = "Hello"

try:
    # int("abc")
    # a+b
    # 1/0
    welcome_message[1]
except ValueError:
    print("ValueError")
except NameError:
    print("NameError")
except ZeroDivisionError:
    print("ZeroDivisionError")
except:
    print("Some other error")
else:
    print("All good")
finally:
    print("Finally")
