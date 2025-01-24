import re

class User:
    def __init__(self, first_name: str, last_name: str, email: str, phone_number: str, address: str):
        self._first_name = first_name
        self._last_name = last_name
        self.email = email
        self.__phone_number = phone_number
        self.address = address




    @property
    def _firstname(self):
        return self.first_name

    @_firstname.setter
    def _firstname(self, name: str):
        if not name.isalpha():
            raise ValueError("Invalid name, name must only contain alphabets")
        if name == '':
            raise ValueError("Invalid name, name must not be empty")
        self.first_name = name


    @property
    def __phone_number(self):
        return self.__phone_number

    @__phone_number.setter
    def __phone_number(self, number):
        if len(number) != 11:
            raise ValueError('Phone number must be 11 digits')

    @property
    def _last_name(self):
        return self.last_name

    @_last_name.setter
    def _last_name(self, name):
        if not name.isalpha():
            raise ValueError("Invalid name, name must only contain alphabets")
        if name == '':
            raise ValueError("Invalid name, name must not be empty")
        self.last_name = name


   # @property
   # def user_email(self):
   #  return self.user_email
   #
   #  @user_email.setter
   #  def user_email(self, email):
   #      if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',email):
   #          raise ValueError("Invalid email")

    def validate_mail(self, email):
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
                raise ValueError("Invalid email")



    def __str__(self):
        return f"{self._first_name} {self._last_name} {self.email} {self.__phone_number} {self.address}"

    def get_full_name(self):
        return f"{self._first_name} {self._last_name}"


