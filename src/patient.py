import random

from src.user import User
import datetime


class Patient(User):
    patients = []
    def __init__(self, first_name:str, last_name:str, date_of_birth:str, gender:str,occupation:str,type_of_illness:str, address:str, email: str, phone_number: str):
        super().__init__(first_name, last_name, email, phone_number, address)
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.type_of_illness = type_of_illness
        self.occupation = occupation
        self.creation_date = datetime.date.today()
        self.patients.append(self)
        self.userId = self.generate_id()


    def __str__(self):
        return f'{super().__str__()}  {self.date_of_birth} {self.gender} {self.occupation} {self.type_of_illness} {self.creation_date}'


    def generate_id(self):
        return random.randrange(1000, 2000)

    def message(self):
        print("You have been registered successfully")
        print(f'your id is : {self.userId}')