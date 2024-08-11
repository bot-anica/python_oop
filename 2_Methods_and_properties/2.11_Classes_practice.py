# Практика: Классы

# Декоратор @property нужен для контроля получения аттрибутов
# Декоратор @propertyname.setter нужен для контроля назначения

class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password  # Set password using @password.setter (line 37)
        self.__secret = "abracadabra"

    @property
    def password(self):
        print("Get password")
        return self.__password

    @property
    def secret(self):
        s = input("Enter your password to get secret: ")
        if s == self.password:
            return self.__secret
        else:
            raise ValueError("Incorrect password")

    @staticmethod
    def is_include_number(value):
        return any(char.isdigit() for char in value)

    @staticmethod
    def check_if_password_is_bad(value):
        with open("bad_passwords.txt", "r") as file:
            for line in file:
                if value in line:
                    return True

        return False

    @password.setter
    def password(self, value):
        print("Set password")

        if not isinstance(value, str):
            raise TypeError("Password must be a string")

        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")

        if not User.is_include_number(value):
            raise ValueError("Password must contain at least one number")

        if User.check_if_password_is_bad(value):
            raise ValueError("Password is bad")

        self.__password = value


# Homework 1

class Registration:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, value):
        if not ("@" in value):
            raise ValueError("Login must include @ symbol")

        if not ("." in value):
            raise ValueError("Login must include . symbol")

        self.__login = value

    @property
    def password(self):
        return self.__password

    @staticmethod
    def is_include_number(value):
        return any(char.isdigit() for char in value)

    @staticmethod
    def is_include_all_register(value):
        is_include_lowercase = any(char.islower() for char in value)
        is_include_uppercase = any(char.isupper() for char in value)
        return is_include_lowercase and is_include_uppercase

    @staticmethod
    def is_include_only_latin_letters(value):
        return all(char.isascii() for char in value)

    @staticmethod
    def is_password_easy(value):
        with open("easy_passwords.txt", "r") as file:
            for line in file:
                if value in line:
                    return True

        return False

    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise TypeError("Password must be a string")

        if len(value) < 5:
            raise ValueError("Password must be at least 5 characters long")

        if len(value) > 11:
            raise ValueError("Password must be at most 11 characters long")

        if not Registration.is_include_number(value):
            raise ValueError("Password must contain at least one number")

        if not Registration.is_include_all_register(value):
            raise ValueError("Password must contain at least one uppercase and one lowercase character")

        if not Registration.is_include_only_latin_letters(value):
            raise ValueError("Password must contain only latin letters")

        if Registration.is_password_easy(value):
            raise ValueError("Password is easy. Please choose another password")

        self.__password = value


user = Registration("wvUeh@example.com", "Qwerty123")
