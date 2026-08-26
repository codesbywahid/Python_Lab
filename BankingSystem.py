# Its a banking system project with OOP concepts


Balance=[]
def deposit():
    amount= int(input("Enter amount to deposit : "))
    if amount>0:
        Balance.append(amount)
        print("Amount Successfully Added")
    elif amount<0:
        print("Enter greater amount")
