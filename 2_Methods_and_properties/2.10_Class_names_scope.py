# Пространство имен КЛАССА

class DepartmentIT:
    PYTHON_DEV = 3
    GO_DEV = 3
    REACT_DEV = 2

    def developers_quantity(self):
        print(self.PYTHON_DEV + self.GO_DEV + self.REACT_DEV)

    def developers_quantity_2(self):
        print(DepartmentIT.PYTHON_DEV + DepartmentIT.GO_DEV + DepartmentIT.REACT_DEV)

    @property
    def developers_quantity_prop(self):
        print(self.PYTHON_DEV + self.GO_DEV + self.REACT_DEV)

    @classmethod
    def developers_quantity_class(cls):
        print(cls.PYTHON_DEV + cls.GO_DEV + cls.REACT_DEV)

    @staticmethod
    def developers_quantity_static():
        print(DepartmentIT.PYTHON_DEV + DepartmentIT.GO_DEV + DepartmentIT.REACT_DEV)

    def hiring_python_developer_in_instance(self):
        self.PYTHON_DEV += 1

    @staticmethod
    def hiring_python_developer_in_class():
        DepartmentIT.PYTHON_DEV += 1


it1 = DepartmentIT()
print("\ndevelopers_quantity")
it1.developers_quantity()
print("\ndevelopers_quantity_2")
it1.developers_quantity_2()
print("\ndevelopers_quantity_prop")
it1.developers_quantity_prop
print("\ndevelopers_quantity_class")
it1.developers_quantity_class()
print("\ndevelopers_quantity_static")
it1.developers_quantity_static()

print("\nhiring_python_developer_in_instance")
print(f"Before: {it1.PYTHON_DEV}")
it1.hiring_python_developer_in_instance()
print(f"After: {it1.PYTHON_DEV}")

print("\nhiring_python_developer_in_class")
print(f"Before: {DepartmentIT.PYTHON_DEV}")
it1.hiring_python_developer_in_class()
print(f"After: {DepartmentIT.PYTHON_DEV}")
