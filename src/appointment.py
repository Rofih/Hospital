import datetime
class Appointment:
    appointments = []
    def __init__(self,patient,user_id,appointment_date,appointment_time,assigned_doctor):
        self.patient_name = patient.get_full_name()
        self.appointment_date = self.create_appointment_date(appointment_date)
        self.appointment_time = appointment_time
        self.assigned_doctor = assigned_doctor
        self.appointments.append(self)

    def create_appointment_date(self,appointment_date):
        array = appointment_date.split('-')
        return datetime.date(int(array[0]),int(array[1]),int(array[2]))

    def __str__(self):
        return f'{self.patient_name} {self.appointment_date} {self.appointment_time} {self.assigned_doctor}'

    def get_assigned_doctor(self):
        return self.assigned_doctor

    def validate_patient(self,patient,user_id):
        for patientz in patient.patients:
            if patientz.get_user_id == user_id:
                return True
            else:
                return False



