import tkinter as tk
import csv

class Patient:
    def __init__(self, name):
        self.name = name

class Doctor:
    def __init__(self, name):
        self.name = name
        self.patient_list = []

    def add_patient(self, patient):
        if len(self.patient_list) < 9:
            self.patient_list.append(patient)
            return True
        return False

def scheduler(patient, doctor):
    if doctor.add_patient(patient):
        schedule_label.config(text="Appointment scheduled.")
        with open('appointments.csv', mode='a') as csv_file:
            fieldnames = ['Patient Name', 'Doctor Name']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writerow({'Patient Name': patient.name, 'Doctor Name': doctor.name})
    else:
        schedule_label.config(text="Doctor's schedule is full.")

def on_submit():
    patient_name = patient_entry.get()
    doctor_name = doctor_var.get()
    if patient_name.strip() == "":
        schedule_label.config(text="Please enter a name.")
    else:
        patient = Patient(patient_name)
        for doctor in doctors_list:
            if doctor.name == doctor_name:
                scheduler(patient, doctor)
                break

root = tk.Tk()
root.title("Patient/Doctor Scheduler")

patient_label = tk.Label(root, text="Patient Name:")
patient_label.grid(row=0, column=0)

patient_entry = tk.Entry(root)
patient_entry.grid(row=0, column=1)

doctor_label = tk.Label(root, text="Doctor Name:")
doctor_label.grid(row=1, column=0)

doctors_list = [Doctor("Dr. Jones"), Doctor("Dr. Smith"), Doctor("Dr. Patel"), Doctor("Dr. Garcia")]
doctor_var = tk.StringVar(root)
doctor_var.set(doctors_list[0].name)

doctor_dropdown = tk.OptionMenu(root, doctor_var, *[doctor.name for doctor in doctors_list])
doctor_dropdown.grid(row=1, column=1)

submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.grid(row=2, column=0, columnspan=2, pady=10)

schedule_label = tk.Label(root, text="12")
schedule_label.grid(row=3, column=0, columnspan=2)

root.mainloop()
