# Hospital Management System
# Lets you add patients, add doctors, schedule appointments, and view appointments.

patients = []
doctors = []
appointments = []

doctors.append({"ID": 1, "Name": "Dr. Waseem", "Specialization": "Physician"})
doctors.append({"ID": 2, "Name": "Dr. Ali", "Specialization": "General"})
doctors.append({"ID": 3, "Name": "Dr. Armaghan", "Specialization": "Specialist"})


def display_patient(p):
    print("Patient -> ID:", p["ID"], ", Name:", p["Name"], ", Age:", p["Age"])


def display_doctor(d):
    print("Doctor -> ID:", d["ID"], ", Name:", d["Name"], ", Specialization:", d["Specialization"])

def add_patient():
    name = input("Enter Patient Name : ")
    age = int(input("Enter Age : "))

    if age <= 0:
        print("Age must be greater than 0")
        return

    new_id = len(patients) + 1
    patients.append({"ID": new_id, "Name": name, "Age": age})
    print("Patient added successfully with ID", new_id)

def add_doctor():
    name = input("Enter Doctor Name : ")
    specialization = input("Enter Specialization : ")

    new_id = len(doctors) + 1
    doctors.append({"ID": new_id, "Name": name, "Specialization": specialization})
    print("Doctor added successfully with ID", new_id)

def schedule_appointment():
    if len(patients) == 0:
        print("Add patients first.")
        return

    print("Select Patient by ID:")
    for p in patients:
        display_patient(p)

    pid = int(input("Enter Patient ID : "))
    selected_patient = None
    for p in patients:
        if p["ID"] == pid:
            selected_patient = p
            break

    if selected_patient is None:
        print("Invalid Patient ID.")
        return

    print("Select Doctor by ID:")
    for d in doctors:
        display_doctor(d)

    did = int(input("Enter Doctor ID : "))
    selected_doctor = None
    for d in doctors:
        if d["ID"] == did:
            selected_doctor = d
            break

    if selected_doctor is None:
        print("Invalid Doctor ID.")
        return

    date_time = input("Enter Appointment Date & Time (e.g., 2025-12-20 10:00 AM) : ")

    appointments.append({
        "Patient": selected_patient,
        "Doctor": selected_doctor,
        "DateTime": date_time
    })
    print("Appointment scheduled successfully!")

def display_appointments():
    if len(appointments) == 0:
        print("No appointments scheduled.")
        return

    for app in appointments:
        print("\n--- Appointment Details ---")
        display_patient(app["Patient"])
        display_doctor(app["Doctor"])
        print("Scheduled Date & Time:", app["DateTime"])
        print("--------------------------")

while True:
    print("\n--- Hospital Management System ---")
    print("1. Add Patient")
    print("2. Add Doctor")
    print("3. Schedule Appointment")
    print("4. Display All Appointments")
    print("5. Exit")

    choice = input("Choose an option : ")

    if choice == "1":
        add_patient()
    elif choice == "2":
        add_doctor()
    elif choice == "3":
        schedule_appointment()
    elif choice == "4":
        display_appointments()
    elif choice == "5":
        print("Exiting system.")
        break
    else:
        print("Invalid choice. Try again.")