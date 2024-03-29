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
import pickle

class Patient:
    """"""
    _next_patient_id = 1
    _all_patients = {}

    def __init__(self, first_name, last_name, address, phone_number, emergency_contact_name, emergency_contact_number):
        """Create a patient

        :param first_name: str
        :param last_name: str
        :param address: str
        :param phone_number: str
        :param emergency_contact_name: str
        :param emergency_contact_number: str
        """
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone_number = phone_number
        self.emergency_contact_name = emergency_contact_name
        self.emergency_contact_number = emergency_contact_number
        self.procedures = []
        self._id = Patient._next_patient_id
        Patient._all_patients[self._id] = self
        type(self)._next_patient_id += 1


    def __str__(self):
        return f"Patient ID: {self._id}\n" \
               f"First Name: {self.first_name}\n" \
               f"Last Name: {self.last_name}\n" \
               f"Address: {self.address}\n" \
               f"Phone Number: {self.phone_number}\n" \
               f"Emergency Contact Name: {self.emergency_contact_name}\n" \
               f"Emergency Contact Phone Number: {self.emergency_contact_number}\n" \
               f"Procedures: {self.procedures}"

    # Matt Compton Helped me with this function specifically the .append, I now realize this is pulled from a list
    def add_procedure(self, procedure):
        self.procedures.append(procedure)

    @classmethod
    def get_patient(cls, patient_id):
        return cls._all_patients.get(patient_id)

    @classmethod
    def delete_patient(cls, patient_id):
        if patient_id in cls._all_patients:
            del cls._all_patients[patient_id]
        else:
            print("Error, ",patient_id," is invalid")

    @classmethod
    def save_patients(cls, data_file):
        """Save patients to file

        :param data_file: (str) filename
        """
        with open(data_file,'wb') as file:
            pickle.dump([Patient._all_patients, Patient._next_patient_id], file)



    @classmethod
    def load_patients(cls, data_file):
        with open(data_file, 'rb') as file:
            Patient._all_patients, Patient._next_patient_id = pickle.load(file)

class Procedure:
    def __init__(self, name, doctor, date, cost, _id, _next_id):
        self.name = name
        self.doctor = doctor
        self.date = date
        self.cost = cost
        self._id = _id
        self._next_id = _next_id
    def __str__(self):
        return f"Name: {self.name}\n" \
               f"Doctor: {self.doctor}\n" \
               f"Date: {self.date}\n" \
               f"Cost: {self.cost}"


if __name__ == "__main__":
    john_doe = Patient('John','Doe','324 st','345-4-3','Mom','32-456-43')
    Patient.save_patients('patient_db.pickle')
    Patient._all_patients = {'bad date':0}
    Patient.load_patients('patient_db.pickle')
    print(Patient.get_patient(1))
