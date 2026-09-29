PROJECT REPORT: PYTHON CONSOLE EXPENSE TRACKER
1. ABSTRACT
The Python Console Expense Tracker is a lightweight, command-line interface (CLI) application developed to assist users in monitoring, recording, and evaluating their day-to-day personal expenditures. Built entirely using core Python constructs without third-party dependencies, this project provides a practical solution for tracking finances in Indian Rupees (INR). It serves as both a functional utility for personal budgeting and an educational model demonstrating fundamental software development principles such as control flow, data structures, and modular design.

2. INTRODUCTION & PROBLEM STATEMENT
2.1 Introduction
In modern life, managing personal finances efficiently is crucial. However, many available software solutions are bloated, requiring cloud accounts, continuous internet connectivity, or complex installations. This project offers a streamlined, offline alternative that operates instantly inside any terminal environment.

2.2 Problem Statement
Individuals frequently struggle to keep track of minor daily cash and digital expenditures (e.g., food, transit, stationery). Without a structured record, unmonitored small purchases accumulate unnoticed, leading to poor budgeting. The objective of this project is to provide a fast, secure, local, and straightforward tool to log and analyze these expenses with zero setup friction.

3. SYSTEM REQUIREMENTS
Programming Language: Python 3.x (Vanilla Python)

Execution Environment: Any OS terminal (Command Prompt, PowerShell, Bash, Zsh) supporting Python.

Dependencies: None (uses built-in modules only).

Storage: In-memory runtime storage using Python lists and dictionaries.

4. SYSTEM DESIGN & ARCHITECTURE
The application follows a procedural, event-driven design pattern structured around a continuous loop control mechanism.

[ User Terminal ] ---> [ Main Menu Loop (while True) ]
                              |
        +---------------------+---------------------+
        |                     |                     |
        v (Choice 1)          v (Choice 2 & 3)      v (Choice 4)
[ Append to Dictionary ] -> [ Read / Calculate ] -> [ Break & Exit ]
        to `expensesLIST`     from `expensesLIST`
5. SOURCE CODE IMPLEMENTATION
Python
expensesLIST = []
print("Welcome to the Expense Tracker!")

while True:
    print("==Menu==:")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expenses")
    print("4. Exit")

    choice = int(input("please Enter your choice (1-4): "))

    if(choice==1): #add expense
        date = input("please enter the date of expense (YYYY-MM-DD): ")
        category = input("please enter the category of expense ( Food, Travel, stationary,etc): ")
        description = input("please give more details about the expense: ")
        amount = float(input("please enter the amount of expense:₹ "))

        expense = {
            'date': date,
            'category': category,
            'description': description,
            'amount': amount
        }
        
        expensesLIST.append(expense)
        print("\nDone , Expense added successfully!")

    elif(choice==2): #view all expenses
        if(len(expensesLIST) == 0):
            print("No expenses seen.")
        else:
            print("Expenses:")
            count = 1
            for every_expense in expensesLIST:
                print(f"{count} - {every_expense['date']} - {every_expense['category']} - {every_expense['description']} - ₹{every_expense['amount']}")
                count += 1

    elif(choice==3): #view total expenses
        total = 0
        for every_expense in expensesLIST:
            total += every_expense["amount"]

        print(f"Total Expenses: ₹{total}")  

    elif(choice==4): #exit
        print("Exiting the Expense Tracker , Goodbye!")
        break

    else:
        print("INVALID CHOICE. Please try again later.")
6. MODULE-WISE CODE REVIEW
Global Initialization: Initializes an empty list expensesLIST to hold transaction dictionaries at runtime.

Control Loop & Menu: An infinite while True loop presenting a 4-option menu. User input is cast to an integer to route conditional logic.

Expense Addition (Choice 1): Collects date, category, description, and amount (cast to float), wraps them in a dictionary, and appends the record to expensesLIST.

Expense Listing (Choice 2): Validates if records exist. If populated, it iterates through the list using an enumerated count and formatted f-strings to display transaction details.

Total Calculation (Choice 3): Iterates through the stored dictionaries, accumulates the amount values, and prints the grand total sum in INR.

Exit & Error Handling (Choice 4 & Else): Choice 4 breaks the loop and terminates execution. Invalid numbers trigger the fallback error message.

7. TESTING & EXECUTION RESULTS
Test Case 1 (Adding Expense): User selects 1, enters valid string/numeric data. Output confirms: Done , Expense added successfully!

Test Case 2 (Viewing Empty List): Selecting 2 when no data exists returns: No expenses seen.

Test Case 3 (Total Calculation): Sums up all amounts accurately with currency formatting (e.g., Total Expenses: ₹310.0).

8. CONCLUSION & FUTURE SCOPE
The Python Console Expense Tracker successfully fulfills its objective of providing a simple, quick, and reliable CLI budgeting tool.

Future Enhancements:

Data Persistence: Integrating Python's json or csv library to save and load records from a local file.

Input Validation: Adding try-except blocks to gracefully handle accidental non-integer menu selections.

Category Filtering: Allowing users to filter expenditure reports by specific categories.
