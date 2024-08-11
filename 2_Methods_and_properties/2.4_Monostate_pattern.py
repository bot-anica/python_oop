# Моносостояние для всех ЭКЗЕМПЛЯРОВ КЛАССА (monostate pattern)

# При изменении аттрибута экземпляра класса, оно измениться только у этого экземпляра
class Dog:
    breed = "Husky"


dog_1 = Dog()
dog_2 = Dog()

dog_1.breed = "Labrador"

print(dog_1.breed)  # "Labrador"
print(dog_2.breed)  # "Husky"


# Моносостояние для всех ЭКЗЕМПЛЯРОВ КЛАССА (monostate pattern)
# При изменении значения общего аттрибута КЛАССА, оно измениться для всех экземпляров
class Cat:
    __shared_attr = {
        "breed": "Persian",
        "color": "black",
    }

    def __init__(self):
        self.__dict__ = Cat.__shared_attr


cat_1 = Cat()
cat_2 = Cat()

cat_1.color = "white"

print(cat_1.color)  # "white"
print(cat_2.color)  # "white"
# Мы изменили значение аттрибута color только для cat_1,
# но так как это общий аттрибут,
# то его значение изменилось и для экземпляров cat_2
