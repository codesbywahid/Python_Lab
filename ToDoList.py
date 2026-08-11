# To do List mini project 

Task = []
while True:
    print("\n===== TO-DO LIST =====\n"
          "\n1. add task"
          "\n2. view tasks"
          "\n3. remove task"
          "\n4. mark task complete"
          "\n5. quit")

    choice = input("Enter your choice : ").lower()

    if choice == "5" or choice == "quit":
        print("Quitting")
        break

    if choice == "1" or choice == "add task":
        task = input("Enter your task : ").strip()
        if not task:
            print("Task cant be empty")
        elif task in Task:
            print("Task already exist")
        else:
            Task.append(task)
            print("Task Added")

    elif choice == "2" or choice == "view tasks":
        if not Task:
            print("No tasks Available")
        else:
            number = 1
            for item in Task:
                print(number, ". ", item)
                number += 1

    elif choice == "3" or choice == "remove task":
        if not Task:
            print("task list is empty")
        else:
            print(Task)

            try:
                delete = int(input("Enter Task number you want to remove : "))
            except ValueError:
                print("Please enter a number : ")
                continue

            index = delete - 1

            if delete >= 1 and delete <= len(Task):
                Task.pop(index)
                print("Task Removed")
            else:
                print("Invalid task number")

    elif choice == "4" or choice == "mark task complete":
        if not Task:
            print("Task list empty")
        else:
            try:
                complete = int(input("Enter task number to complete : "))
            except ValueError:
                print("Please enter a number : ")
                continue

            index = complete - 1
            if complete >= 1 and complete <= len(Task):
                if " ✔️" in Task[index]:
                    print("Task already completed ")
                else:
                    Task[index] = Task[index] + " ✔️"
                    print("Task Marked as complete")
            else:
                print("Invalid task number")

    else:
        print("Invalid choice. Enter choice again : ")