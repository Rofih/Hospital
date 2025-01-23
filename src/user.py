import re

class User:
    def __init__(self, first_name: str, last_name: str, email: str, phone_number: str, address: str):
        self.__first_name = first_name
        self.__last_name = last_name
        self.email = email
        self.__phone_number = phone_number
        self.address = address




    @property
    def __firstname(self):
        return self.__first_name

    @property
    def __phone_number(self):
        return self.__phone_number

    @__phone_number.setter
    def __phone_number(self, number):
        if len(number) != 11:
            raise ValueError('Phone number must be 11 digits')
        self.__phone_number = number

    @property
    def __last_name(self):
        return self.__last_name

    @__last_name.setter
    def __last_name(self, last_name):
            self.__last_name = self.validate_last_name(last_name)

    def validate_phone_number(self, phone_number):
        length = len(phone_number)
        if length != 11:
            return "Invalid phone number"

    def validate_mail(self, email):
        valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)
        return email if valid else "invalid email"

    def validate_first_name(self, name):
        if not name.isalpha():
            raise ValueError("Invalid name, name must only contain alphabets")
        if name == '':
            raise ValueError("Invalid name, name must not be empty")
        self.__first_name = name


    def validate_last_name(self, name):
        if not name.isalpha():
            raise ValueError("Invalid name, name must only contain alphabets")
        if name == '':
            raise ValueError("Invalid name, name must not be empty")
        self.__first_name = name

    def __str__(self):
        return f"{self.__first_name} {self.__last_name} {self.email} {self.__phone_number} {self.address}"

    def get_full_name(self):
        return f"{self.__first_name} {self.__last_name}"


