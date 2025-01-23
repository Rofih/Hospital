import unittest
from src import user

class TestUser(unittest.TestCase):
    def test_that_User_class_exist(self):
        # user_class = User
        user.User("Eniola","Olamide","email@yahoo.com","3636373838","lagos")
    def test_that_User_has_a_unique_id(self):
        person = user.User("Eniola", "Olamide", "email@yahoo.com", "3636373838", "lagos")
        print(person.get_user_id())


    def test_that_email_Is_valid(self):
        person = user.User("Eniola", "Olamide", "emailyahoo.com", "3636373838", "lagos")
        message = "invalid email"
        self.assertEqual(message,person.email)
        person2 = user.User("Eniola", "Olamide", "email@yahoo.com", "3636373838", "lagos")
        message2 = "valid email"
        self.assertEqual(message2, person2.email)

    def test_that_phone_number_Is_valid(self):
        person = user.User("Eniola", "Olamide", "email@yahoo.com", "3636373838", "lagos")
        message = "Invalid phone number"
        self.assertEqual(message, person.phone_number)

    def test_that_name_Is_valid(self):
        person = user.User("838383838383", "olamide", "email@yahoo.com", "09127461933", "lagos")
        message = "invalid name"
        self.assertEqual(message, person.first_name)
        person2 = user.User("Eniola", "Olamide", "email@yahoo.com", "09127461933", "lagos")
        message2 = "valid name"
        self.assertEqual(message2, person2.first_name)





