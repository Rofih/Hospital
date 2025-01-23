import unittest

from src.reception import Reception


class MyTestCase(unittest.TestCase):
    # def test_that_i_can_register_doctor(self):
    #     reception = Reception()
    #     reception.register_doctor("Rofih","Olamide","email@yahoo.com","09127461933","surgeon","lagos")
    #     number_of_doctors = 1
    #     self.assertEqual(number_of_doctors, len(reception.list_of_doctors))

    def test_that_i_can_get_doctors_info(self):
        reception = Reception()
        reception.register_doctor("55656666666","Olamide","email@yahoo.com","09127461933","surgeon","lagos")
        doctor_id = reception.user_id
        doctor_info = reception.get_doctor_info(doctor_id)
        print(doctor_info)



if __name__ == '__main__':
    unittest.main()
