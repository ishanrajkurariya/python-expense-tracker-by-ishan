expenselist=[0]
# EXPENSE TRACKER PROJECT :-


expensesLIST=[]
print("Welcome to the Expense Tracker!")

while True:
    print("==Menu==:")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expenses")
    print("4. Exit")

    choice = int(input("please Enter your choice (1-4): "))

    if(choice==1): #add expense
        date=input("please enter the date of expense (YYYY-MM-DD): ")
        category=input("please enter the category of expense ( Food, Travel, stationary,etc): ")
        description=input("please give more details about the expense: ")
        amount=float(input("please enter the amount of expense:₹ "))

        expense={
            'date': date,
            'category': category,
            'description': description,
            'amount': amount}
        
        expensesLIST.append(expense)
        print("\nDone , Expense added successfully!")

    elif(choice==2): #view all expenses
        if(  len(expensesLIST)==0):
            print("No expenses seen.")
        else:
            print("Expenses:")
            count=1
            for every_expense in expensesLIST:
                print(f"{count} - {every_expense["date"]} - {every_expense["category"]} - {every_expense["description"]} - ₹{every_expense["amount"]}")
                count+=1


    elif (choice==3): #view total expenses
        total=0
        for every_expense in expensesLIST:
            total+= every_expense["amount"]

        print(f"Total Expenses: ₹{total}")  

    elif (choice==4): #exit
        print("Exiting the Expense Tracker , Goodbye!")
        break
            

    else:
        print("INVALID CHOICE. Please try again later.")