from src.reception import Reception

reception = Reception()



def register_patient():
    print("You are welcome to Redditon Hospital")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")
    phone_number = input("Enter your phone number: ")
    date_of_birth = input("Enter your date of birth: ")
    gender = input("Enter your gender: ")
    occupation = input("Enter your occupation: ")
    type_of_illness = input("Enter your type of illness: ")
    address = input("Enter your address: ")
    print("your healing is our priority")
    reception.register_patient(first_name, last_name, date_of_birth, gender,occupation,type_of_illness, address, email, phone_number)
    menu()


def register_doctor():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")
    phone_number = input("Enter your phone number: ")
    role = input("Enter your area_of_specialization: ")
    address = input("Enter your address: ")
    reception.register_doctor(first_name, last_name, email, phone_number, role, address)
    menu()


def book_appointment():
    user_id = input("Enter your user id: ")
    appointment_date = input("Enter your appointment date: ")
    appointment_time = input("Enter your appointment time: ")
    assigned_doctor = input("Enter the assigned doctor: ")
    reception.book_appointment(user_id, appointment_date, appointment_time, assigned_doctor)
    menu()


def get_patient_details():
    user_id = input("Enter your patient id: ")
    reception.get_patient_info(user_id)
    menu()


def get_doctor_info():
    user_id = input("Enter your doctor id: ")
    reception.get_doctor_info(user_id)
    menu()


def get_doctors():
    reception.get_list_of_doctors()
    menu()


def menu():
    option ="""1-> register patient
            2->register doctor
            3->book-appointment
            4-> patient details
            5-> doctor information
            6-> list of doctors
            """
    print(option)
    selected_option = input("enter yor option: ")

    match selected_option:
        case "1":register_patient()
        case "2":register_doctor()
        case "3":book_appointment()
        case "4":get_patient_details()
        case "5":get_doctor_info()
        case "6":get_doctors()


if __name__ == "__main__":
    menu()