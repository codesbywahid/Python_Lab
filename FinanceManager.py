# Personal Finance Manager Project :

from datetime import datetime
transactions = []
budgets = {}

def add_income():
    desc = input("Enter your income description : ")

    while True:
        try:
            amount = int(input("Enter your income amount : "))
        except ValueError:
            print("Enter a numeric value")
            continue
        if amount <= 0:
            print("Enter amount greater than 0 ")
        else:
            print("Amount added")
            break
    categ = input("Enter income Category : ")
    while True:
        try:
            Date = input("Enter date in this format YYYY-MM-DD : ")
            datetime.strptime(Date, "%Y-%m-%d")
        except ValueError:
            print("Enter proper date ")
            continue
        else:
            break
    dic = {
        "Description": desc,
        "Amount": amount,
        "Category": categ,
        "Date": Date,
        "Type": "Income"
    }
    transactions.append(dic)
    print("Successfully added")

def add_expense():
    desc = input("Enter expense Description : ")
    while True:
        try:
            amount= int(input("Enter your expense amount : "))
        except ValueError:
            print("Enter a numeric value")
            continue
        if amount<=0:
            print("Enter amount greater than 0 ")
        elif amount >0:
            print("Amount added")
            break

    categ=input("Enter expense Category : ")
    while True:
            try:
                Date = input("Enter date in this format YYYY-MM-DD : ")
                datetime.strptime(Date, "%Y-%m-%d")
            except ValueError:
                print("Enter proper date ")
                continue
            else:
                break
    dic={
            "Description" : desc,
            "Amount" : amount,
            "Category" : categ,
            "Date" : Date,
            "Type" : "Expense"
        }
    transactions.append(dic)
    print("Successfully added")

def view_transactions():
    if not transactions:
        print("There are no transactions")
    else:
        number = 1
        for transaction in transactions:
            print(number," ",transaction["Description"])
            print(number," ",transaction["Amount"])
            print(number," ",transaction["Category"])
            print(number," ",transaction["Date"])
            print(number," ",transaction["Type"])
            number+=1

def delete_transactions():
    if not transactions:
        print("No transaction found to delete")
    else:
        view_transactions()
        try:
            choice=int(input("Enter transaction you want to delete : "))
        except ValueError:
            print("Please enter a numeric value")
            return
         
        index = choice-1
        if 1<= choice <= len(transactions):
            transactions.pop(index)
            print("Transaction deleted successfully") 
        else:
            print("Invalid choice. ")

def view_balance():
    if not transactions:
        print("No balance found")
    else:
        total_income=0
        total_expenses=0
        for transaction in transactions:
            if transaction["Type"]=="Income":
                total_income+= transaction["Amount"]
            elif transaction["Type"]=="Expense":
                total_expenses+=transaction["Amount"]

            Balance=total_income-total_expenses
            print("Total Income is : ",total_income)
            print("Total Expense is : ",total_expenses)
            print("Available Balance is : ",Balance)

def view_by_category():
    if not transactions:
        print("No transactions found")
    else:
        total_spent=0
        choice=input("Enter a category you want to view : ")
        found=False
        for transaction in transactions:
            if transaction["Type"] == "Expense" and transaction["Category"]==choice:
                found=True
                print(transaction)
                total_spent+=transaction["Amount"]
        if not found:
                print("None expenses found")
        else:
            print("Total spending in this category is : ",total_spent)

def set_budget():
    choice=input("Enter category you want to set budget for : ")
    while True:
        try:
            amount=int(input("Enter budget amount : "))
            
        except ValueError:
            print("Enter a numeric value")
            continue
        if amount<=0:
            print("Enter greater amount")
        else:
            break
    budgets[choice]=amount
    print("Budget added successfully")

def view_budget_status():
    if not budgets:
        print("No budgets found")
    else:
        number = 1
        for category in budgets:
            budget_amount = budgets[category]
            total_spent = 0
            for transaction in transactions:
                if transaction["Type"] == "Expense" and transaction["Category"] == category:
                    total_spent += transaction["Amount"]
            remaining = budget_amount - total_spent
            print(number, " ", category)
            print("Budget:", budget_amount)
            print("Spent:", total_spent)
            print("Remaining:", remaining)
            if total_spent > budget_amount:
                print("Category is over budget")
            number += 1


def monthly_summary():
    try:
        month = int(input("Enter month you want to view : "))
        year = int(input("Enter year : "))
    except ValueError:
        print("Enter correct Month / Year")
        return
    if month < 1 or month > 12:
        print("Enter month between 1-12")
        return
    income = 0
    expenses = 0
    found = False
    for transaction in transactions:
        transaction_date = datetime.strptime(
            transaction["Date"], "%Y-%m-%d"
        )
        if transaction_date.year == year and transaction_date.month == month:
            found = True
            if transaction["Type"] == "Income":
                income += transaction["Amount"]
            elif transaction["Type"] == "Expense":
                expenses += transaction["Amount"]
    if not found:
        print("No transactions found for this month")
        return
    monthly_balance = income - expenses
    print("Total Income is : ", income)
    print("Total Expense is : ", expenses)
    print("Monthly Balance is : ", monthly_balance)

def search_transactions():
    choice=input("Enter transaction you want to search for : ").lower()
    found = False
    for transaction in transactions:
        if choice in transaction["Description"].lower() or choice in transaction["Category"].lower() :
            found=True
            print(transaction)
    if not found:
            print("No matching transactions found")

def edit_transaction():
    if not transactions:
        print("No transactions found")
    else:
        number = 1

        for transaction in transactions:
            print(number, transaction)
            number += 1

        try:
            choice = int(input("Enter transaction number you want to edit"))
            if choice < 1 or choice > len(transactions):
                print("Enter valid choice number ")
                return
        except ValueError:
            print("Enter a numeric value")

        index = choice - 1
        selected_transaction = transactions[index]

        desc = input("Enter new description : ")
        selected_transaction["Description"] = desc

        while True:
            try:
                amount = int(input("Enter new amount : "))
            except ValueError:
                print("Enter numeric value")
                continue

            if amount <= 0:
                print("Enter amount greater than 0")
                continue

            break
        selected_transaction["Amount"] = amount

        new_categ=input("Enter new category")
        selected_transaction["Category"]=new_categ

    while True:
        try:
            new_date=input("Enter new date in format YYYY-MM-DD")
            datetime.strptime(new_date, "%Y-%m-%d")
        except ValueError:
            print("Enter date in valid format")
            continue
        break

    selected_transaction["Date"]=new_date

print("Transaction Updated Succcessfully")

def filter_transaction():
    if not transactions:
        print("No transactions found")
    else:
        choice = input("Enter type to filter income/expense : ").lower()
        if choice not in ["income","expense"]:
            print("Enter income or expense ")
            return
        found=False
        for transaction in transactions:
            if transaction["Type"].lower()==choice:
                found=True
                print(transaction)
        if not found:
            print("No matching transaction found")

def transaction_stats():
    if not transactions:
        print("No transactions found")
    else:
        total_transactions = len(transactions)
        total_income = 0
        total_expenses = 0
        expense_count = 0
        highest_expense = None
        lowest_expense = None

        for transaction in transactions:
            if transaction["Type"] == "Income":
                total_income += transaction["Amount"]

            elif transaction["Type"] == "Expense":
                total_expenses += transaction["Amount"]
                expense_count += 1

                if highest_expense is None or transaction["Amount"] > highest_expense:
                    highest_expense = transaction["Amount"]

                if lowest_expense is None or transaction["Amount"] < lowest_expense:
                    lowest_expense = transaction["Amount"]

        print("Your Total transactions are : ", total_transactions)
        print("Your Total income is : ", total_income)
        print("Your Total expense is : ", total_expenses)
        print("Your Total expense count is : ", expense_count)
        print("Your highest expense is : ", highest_expense)
        print("Your lowest expense is : ", lowest_expense)

        if expense_count > 0:
            average_expense = total_expenses / expense_count
            print("Your average expense is : ", average_expense)
        else:
            print("No expenses found")

while True:
    print("\n===== Personal Finance Manager =====\n")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. Delete Transaction")
    print("5. Edit Transaction")
    print("6. View Balance")
    print("7. View Spending by Category")
    print("8. Set Budget")
    print("9. View Budget Status")
    print("10. Monthly Summary")
    print("11. Search Transactions")
    print("12. Filter Transactions")
    print("13. Transaction Statistics")
    print("14. Exit")

    choice = input("Enter your choice : ")

    if choice == "1":
        add_income()

    elif choice == "2":
        add_expense()

    elif choice == "3":
        view_transactions()

    elif choice == "4":
        delete_transactions()

    elif choice == "5":
        edit_transaction()

    elif choice == "6":
        view_balance()

    elif choice == "7":
        view_by_category()

    elif choice == "8":
        set_budget()

    elif choice == "9":
        view_budget_status()

    elif choice == "10":
        monthly_summary()

    elif choice == "11":
        search_transactions()

    elif choice == "12":
        filter_transaction()

    elif choice == "13":
        transaction_stats()

    elif choice == "14":
        print("Thank you for using Personal Finance Manager!")
        break

    else:
        print("Invalid choice. Please select a number from 1-14.")