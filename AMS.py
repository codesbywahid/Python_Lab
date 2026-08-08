# Academy Management System 
students = []
teachers = []

courses = ["Java", "Web Development", "Graphic Design", "Cyber Security"]

while True:
    print("""
---Academy Management System---
1. Register Student
2. Register Teacher
3. Display All Students
4. Display All Teachers
5. Search Student by ID
6. Delete Student
7. Delete Teacher
8. Exit
""")
    choice = input("Enter your choice : ")

    if choice == "1":
        Name = input("Enter Student Name : ")
        Age = input("Enter Age : ")
        Id = input("Enter Student ID : ")
        Phone = input("Enter Phone : ")
        Email = input("Enter Email : ")
        print("Available Courses:", courses)
        Course = input("Enter Course : ")

        student = {
            "Name": Name,
            "Age": Age,
            "ID": Id,
            "Phone": Phone,
            "Email": Email,
            "Course": Course
        }
        students.append(student)
        print("Student Registered!")

    elif choice == "2":
        Name = input("Enter Teacher Name : ")
        Age = input("Enter Age : ")
        Subject = input("Enter Subject : ")
        Salary = input("Enter Salary : ")
        Phone = input("Enter Phone : ")
        Email = input("Enter Email : ")
        print("Available Courses:", courses)
        Course = input("Enter Course Teaching : ")
        Timing = input("Enter Timing (Morning/Evening) : ")

        teacher = {
            "Name": Name,
            "Age": Age,
            "Subject": Subject,
            "Salary": Salary,
            "Course": Course,
            "Timing": Timing,
            "Phone": Phone,
            "Email": Email
        }
        teachers.append(teacher)
        print("Teacher Registered!")

    elif choice == "3":
        if not students:
            print("No students registered.")
        else:
            for s in students:
                print("Name:", s["Name"])
                print("Age:", s["Age"])
                print("ID:", s["ID"])
                print("Course:", s["Course"])
                print("Phone:", s["Phone"])
                print("Email:", s["Email"])
                print()

    elif choice == "4":
        if not teachers:
            print("No teachers registered.")
        else:
            for t in teachers:
                print("Name:", t["Name"])
                print("Age:", t["Age"])
                print("Subject:", t["Subject"])
                print("Salary:", t["Salary"])
                print("Course:", t["Course"])
                print("Timing:", t["Timing"])
                print("Phone:", t["Phone"])
                print("Email:", t["Email"])
                print()

    elif choice == "5":
        search_id = input("Enter Student ID to search : ")
        found = False
        for s in students:
            if s["ID"] == search_id:
                print("Student Found")
                print("Name:", s["Name"])
                print("Age:", s["Age"])
                print("ID:", s["ID"])
                print("Course:", s["Course"])
                print("Phone:", s["Phone"])
                print("Email:", s["Email"])
                found = True
        if found == False:
            print("Student not found")

    elif choice == "6":
        delete_id = input("Enter Student ID to delete : ")
        found = False
        for s in students:
            if s["ID"] == delete_id:
                students.remove(s)
                found = True
                break
        if found:
            print("Student Deleted!")
        else:
            print("Student ID not found!")

    elif choice == "7":
        delete_name = input("Enter Teacher Name to delete : ")
        found = False
        for t in teachers:
            if t["Name"].lower() == delete_name.lower():
                teachers.remove(t)
                found = True
                break
        if found:
            print("Teacher Deleted!")
        else:
            print("Teacher name not found!")

    elif choice == "8":
        print("Exiting")
        break