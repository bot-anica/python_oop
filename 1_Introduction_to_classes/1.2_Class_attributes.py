# Аттрибуты классов
from pprint import pprint


# Пример класса с аттрибутами
class Person:
    name = "John"
    age = 36


# Посмотреть список всех аттрибутов КЛАССА можно используя метод __dict__
print(Person.__dict__)

# Посмотреть значение аттрибута КЛАССА можно используя его имя после точки
print(Person.name)
print(Person.age)

# Если аттрибут КЛАССА может отсутствовать, то используя метод getattr можно получить значение по умолчанию
print(getattr(Person, 'sex', 'male'))

# Задать значение аттрибута КЛАССА можно двумя способами:
# - с помощью указания его имени через точку
# - с помощью метода setattr
Person.age += 1
setattr(Person, 'sex', 'male')
pprint(Person.__dict__)

# Удалить аттрибут КЛАССА можно двумя способами:
# - использовать метод del
# - удалить аттрибут с помощью метода delattr
del Person.sex
delattr(Person, 'age')
pprint(Person.__dict__)


# Изменение атрибутов КЛАССА влияет и на ЭКЗЕМПЛЯРЫ КЛАССА
# Если добавить, удалить или изменить аттрибуты класса, то на ЭКЗЕМПЛЯРЫ КЛАССА тоже будут изменены

# Если добавить, удалить или изменить аттрибуты ЭКЗЕМПЛЯРЫ КЛАССА,
# то эти изменения отобразятся только в этом экземпляре


class Cat:
    name = "Garfield"
    color = "black"


my_cat = Cat()
