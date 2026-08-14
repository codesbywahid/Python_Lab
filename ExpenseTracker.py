# Expense Tracker Python Project

expenses = []
def add_expense():
    while True:
        desc = input("Enter expense description : ").strip()

        if desc:
            break
        else:
            print("Description cannot be empty")
    while True:
        try:
            price = int(input("Enter amount of expense : "))

            if price > 0:
                break
            else:
                print("Amount must be greater than 0")

        except ValueError:
            print("Please Enter numeric value")
    while True:
        categ = input("Enter category of expense : ").strip()

        if categ:
            categ = categ.title()
            break
        else:
            print("Category cannot be empty")
    dic = {
        "Description": desc,
        "Amount": price,
        "Category": categ
    }
    expenses.append(dic)
    print("Expense added successfully")

def view_expenses():
    if not expenses:
        print("No expenses to view")
    else:
        Num = 1

        for expense in expenses:
            print(
                Num,
                ".",
                expense["Description"],
                "| Amount:",
                expense["Amount"],
                "| Category:",
                expense["Category"]
            )
            Num += 1

def delete_expense():
    if not expenses:
        print("No expenses available to delete")
    else:
        view_expenses()
        while True:
            try:
                num = int(input("Enter expense number you want to delete : "))

                if 1 <= num <= len(expenses):
                    index = num - 1
                    expenses.pop(index)
                    print("Expense deleted successfully")
                    break
                else:
                    print("Please enter a valid expense number")

            except ValueError:
                print("Please enter a numeric value")

def total_spending():
    if not expenses:
        print("No expenses available")
    else:
        Total = 0
        for expense in expenses:
            Total += expense["Amount"]
        print("Total Spending is :", Total)

def view_by_category():
    if not expenses:
        print("No expenses available")
    else:
        while True:
            choice = input(
                "Enter category you want to see expense of : "
            ).strip()
            if choice:
                choice = choice.title()
                break
            else:
                print("Category cannot be empty")
        Total = 0
        found = False
        for expense in expenses:
            if choice == expense["Category"]:
                found = True
                print(
                    expense["Description"],
                    "| Amount:",
                    expense["Amount"],
                    "| Category:",
                    expense["Category"]
                )
                Total += expense["Amount"]
        if not found:
            print("No expenses found in this category")
        else:
            print("Total spending for this category is :", Total)

while True:
    print(
        "\n==== Expense Tracker ====\n"
        "1. Add Expense\n"
        "2. View Expenses\n"
        "3. Delete Expense\n"
        "4. View Total Spending\n"
        "5. View Spending by Category\n"
        "6. Quit"
    )
    try:
        choice = int(input("Enter Your Choice : "))
    except ValueError:
        print("Please Enter a number from 1 to 6")
        continue
    if choice == 1:
        add_expense()
    elif choice == 2:
        view_expenses()
    elif choice == 3:
        delete_expense()
    elif choice == 4:
        total_spending()
    elif choice == 5:
        view_by_category()
    elif choice == 6:
        print("Good Bye")
        break
    else:
        print("Invalid Choice. Enter a number from 1 to 6")