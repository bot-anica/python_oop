# ? Инструкция raise

try:
    raise ValueError("Some value error")
except ValueError as ve:
    try:
        raise TypeError("Some type error")
    except TypeError as te:
        # Выведется весь стек ошибок: ValueError -> TypeError -> Exception
        # raise Exception("Big exception")

        # Если добавить "from None", то выведется только Exception
        # raise Exception("Big exception") from None

        # Если добавить "from ve" (ValueError), то выведется стек ошибок: ValueError -> Exception
        # raise Exception("Big exception") from ve

        # Если добавить "from te" (TypeError), то выведется стек ошибок: ValueError -> TypeError -> Exception
        raise Exception("Big exception") from te
