# Hospital management system
import pprint
from typing import List


class Patient:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def patient_data(self):
        print('Patient :', self.name)
        print('Age :', self.age)
        print('Gender :', self.gender)


class Doctor:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization
        self.patients = []
        # self.appointments = []

    def add_patient(self, patient: Patient):
        self.patients.append({"patient_name": patient.name,
                              "age": patient.age,
                              "gender": patient.gender})

    def show_all_patients(self):
        pprint.pprint(self.patients, sort_dicts=False)


class Appointment:
    def __init__(self, doctor: Doctor, patient: Patient, date_time):
        self.doctor = doctor.name
        self.patient = patient.name
        self.date_time = date_time

        print(f"{self.doctor} has given the appointment to patient {self.patient} at this time {self.date_time}")


class Billing:
    def __init__(self, patient: Patient):
        self.patient_name = patient.name
        self.total_bill = 0

    def calculate_bills(self, bill_list: List):
        self.total_bill = sum(bill_list)
        print(self.total_bill)


if __name__ == '__main__':
    p1 = Patient("Arshad", 23, "Male")
    d1 = Doctor("Dr.Mannan Khan", "Physician")
    # ap1 = Appointment(d1, p1, "2024-04-01 10:00 AM")
    d1.add_patient(Patient("Sarfaraz", 26, "Male"))
    d1.add_patient(Patient("Aksha", 22, "Female"))
    d1.add_patient(Patient("Hameed", 25, "Male"))
    d1.add_patient(p1)
    d1.show_all_patients()
