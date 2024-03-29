"""DESCRIPTION OF THE MODULE GOES HERE

Author: James Nicholls
Class: CSI-260-01
Assignment: Week 4 Lab
Due Date: September 29, 2023 1:00 PM

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)
"""

from medical import Patient, Procedure

def menu():
    print("Main Menu")
    print("1. Look up patient by ID Number")
    print("2. Add a new patient")
    print("3. Quit")

def patient_lookup():
    patent_id = int(input("Enter patient ID: "))
    patient = Patient.get_patient(patent_id)
    if patient:
        print(patient)
    else:
        print("Patient not found.")

def add_new_patient():
    first_name = input("Enter patient's first name: ")
    last_name = input("Enter patient's last name: ")
    address = input("Enter patient's address: ")
    phone_number = input("Enter patient's phone number: ")
    emergency_contact_name = input("Enter emergency contact's name")
    emergency_contact_number = input("Enter emergency contact's phone number: ")

    patient = Patient(first_name, last_name, address, phone_number, emergency_contact_name, emergency_contact_number)
    print(f"New patient added with ID: {patient.id}")