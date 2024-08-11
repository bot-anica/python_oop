from time import perf_counter


# ? Метод __call__

# __call__ - вызов объекта как функции


class Counter:
    def __init__(self):
        self.counter = 0
        self.counter_sum = 0
        self.counter_length = 0
        print('init object', self)

    # *args - позиционные аргументы
    # **kwargs - именованные аргументы с ключами
    def __call__(self, *args, **kwargs):
        self.counter += 1
        self.counter_sum += sum(args)
        self.counter_length += len(args)
        print(f"\nCounter: {self.counter}\nSum: {self.counter_sum}\nLength: {self.counter_length}")

    def average(self):
        return self.counter_sum / self.counter_length


c = Counter()
c()
c()
c()

c(1, 2, 3, a=1, b=2)
c(5, 6, 7, 8)

print(c.average())


# * Использование метода call в качестве декоратора

class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = perf_counter()
        print("Call function", self.func.__name__)
        result = self.func(*args, **kwargs)
        finish = perf_counter()
        print(f"Time: {finish - start}")
        return result


def factorial(n):
    pr = 1
    for i in range(1, n + 1):
        pr *= i
    return pr


# * Декорируем функцию как объект и вызываем метод __call__
factorial = Timer(factorial)

print("\nFactorial")
print(factorial(1000))


# * Декорируем функцию с помощью декоратора @Timer

@Timer
def fibonachi(n):
    prev = 1
    current = 1
    for i in range(n):
        if i > 1:
            prev, current = current, prev + current

    return current


print("\nFibonachi")
print(fibonachi(500))


# Homework 1

class Addition:
    @staticmethod
    def filter_args(*args):
        filtered_args = []

        for item in args:
            if isinstance(item, int) or isinstance(item, float):
                filtered_args.append(item)

        return filtered_args

    def __call__(self, *args, **kwargs):
        filtered_args = Addition.filter_args(*args)
        print(f"Addition: {sum(filtered_args)}")


print("\nHomework 1")
add = Addition()

add(10, 20)
add(1, 2, 3.4)
add(1, 2, "hello", [1, 2], 3)
