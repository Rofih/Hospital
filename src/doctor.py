import random

from src.user import User


class Doctor(User):
    doctors = []

    def __int__(self):
        self.__doctor = "default"


    def __init__(self, first_name: str, last_name: str, email: str, phone_number: str,role:str, address: str):
        super().__init__(first_name, last_name, email, phone_number, address)
        self.area_of_specialization = role
        self.doctors.append(self)
        self.userId = self.generate_id()


    def __str__(self):
        return f'{super().__str__()} {self.area_of_specialization}'

    def generate_id(self):
        return random.randrange(1000, 2000)

    def message(self):
        print("You have been registered successfully")
        print(f'your id is : {self.userId}')