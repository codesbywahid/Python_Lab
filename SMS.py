Students = []
while True:
    print(""" ---Student Menu---
    1. Add Student
    2. View Students
    3. Search Student
    4. Calculate Average Marks
    5. Show Topper
    6. Exit""")
    x = input("Enter your choice : ")
    if (x == "1"):
        Name = input("Enter Student Name : ")
        Age = int(input("Enter Age : "))
        Marks = int(input("Enter Marks : "))
        Stu = {
            "Name": Name,
            "Age": Age,
            "Marks": Marks
        }
        Students.append(Stu)
    elif (x == "2"):
        for s in Students:
            print("Name:", s["Name"])
            print("Age:", s["Age"])
            print("Marks:", s["Marks"])
    elif (x == "3"):
        y = input("Enter Student Name to search : ")
        found = False
        for s in Students:
            if s["Name"] == y:
                print("Student Found")
                print("Name:", s["Name"])
                print("Age:", s["Age"])
                print("Marks:", s["Marks"])
                found = True
        if found == False:
            print("Student not found")
    elif (x == "4"):
        if not Students:
            print("No Students added yet")
        else:
            Total = 0
            for m in Students:
                Total = Total + m["Marks"]
            Average = Total / len(Students)
            print("Average Marks are : ", Average)
    elif (x == "5"):
        if not Students:
            print("No Students added yet")
        else:
            Topper = Students[0]
            for t in Students:
                if t["Marks"] > Topper["Marks"]:
                    Topper = t
            print("Topper is : ", Topper["Name"])
            print("Age:", Topper["Age"])
            print("Marks:", Topper["Marks"])
    elif (x == "6"):
        print("Exiting")
        break