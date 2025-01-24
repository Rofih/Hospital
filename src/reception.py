from src.appointment import Appointment
from src.doctor import Doctor
from src.patient import Patient


class Reception:

    def __init__(self):
        self.new_patient = None
        self.new_doctor = None
        self.user_id = 0

    def register_doctor(self,first_name: str, last_name: str, email: str, phone_number: str,role:str, address: str):
        self.new_doctor = Doctor(first_name, last_name, email, phone_number, role, address)
        # self.user_id = self.new_doctor.userId()
        self.new_doctor.message()

    def register_patient(self,first_name:str, last_name:str, date_of_birth:str, gender:str,occupation:str,type_of_illness:str, address:str, email: str, phone_number: str):
        self.new_patient = Patient(first_name, last_name, date_of_birth, gender,occupation,type_of_illness, address, email, phone_number)
        self.new_patient.message()



    def book_appointment(self,user_id,appointment_date,appointment_time,assigned_doctor):
        status = self.validate_registration_of_patient(user_id)
        if status:
            new_appointment = Appointment(self.new_patient,user_id, appointment_date, appointment_time,assigned_doctor)
            print("appointment has been booked successfully")
            print(f'your appointment date is:{new_appointment.appointment_date}')
        else:
            print("you need to register to continue")

    def get_patient_info(self,patient_id):
        for patient in self.new_patient.patients:
            if patient.userId() == patient_id:
                return patient.__str__()

    def get_doctor_info(self,doctor_id):
        for doctor in self.new_doctor.doctors:
            if doctor.get_user_id() == doctor_id:
                return doctor.__str__()

    def get_list_of_patients(self):
        for patient in self.new_patient.patients:
            print(patient.__str__())

    def get_list_of_doctors(self):
        for doctor in self.new_doctor.doctors:
            print(doctor.__str__())

    def validate_registration_of_patient(self,user_id):
        for patient in self.new_patient.patients:
            if patient.get_user_id() == user_id:
                return True
            else:
                return False