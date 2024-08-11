# ? Пользовательские исключения

# Мы можем указать родительский класс Exception
#   или какой-нибудь другой конкретный класс,
#   например, ValueError
class MyException(Exception):
    """this is my first exception"""

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'MyException {self.message}'
        else:
            return 'MyException is empty'


raise MyException("Hello")


# * Пример пользовательского исключения для игры Snake

class SnakeExceptionBase(Exception):
    """Основной класс ошибок Змейки"""


class SnakeBorderException(SnakeExceptionBase):
    """Ошибка соприкосновений змейки со стенкой"""


class SnakeTailException(SnakeExceptionBase):
    """Ошибка соприкосновений змейки со своим хвостом"""
