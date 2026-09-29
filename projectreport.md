
# PROJECT REPORT: EXPENSE TRACKER

**Author:** ISHAN RAJ KURARIYA

## 1. Cover Page & Info

* **Project Title:** Python Console Expense Tracker
* **Language:** Python 3.x (Vanilla CLI)

## 2. Introduction & Problem Statement

* **Introduction:** A lightweight offline CLI application to log and manage personal expenses in INR.
* **Problem Statement:** Eliminates manual bookkeeping friction and avoids heavy, bloated finance software.

## 3. Requirements

* **Functional:** Add expense, view all, view total, exit, handle invalid inputs.
* **Non-functional:** Offline accessibility, zero third-party dependencies, high execution speed.

## 4. System Architecture & Design

* **Architecture:** Event-driven procedural loop routing inputs through conditional branches.
* **Data Schema:** List of dictionaries (`expensesLIST` holding `expense` key-value records).

## 5. Implementation Code Snippet

```python
expensesLIST = []
while True:
    choice = int(input("1.Add 2.View 3.Total 4.Exit: "))
    if choice == 1:
        expensesLIST.append({'date': input("Date: "), 'amount': float(input("Amount: ₹"))})
    elif choice == 2: print(expensesLIST)
    elif choice == 3: print(sum(e['amount'] for e in expensesLIST))
    elif choice == 4: break

```

## 6. Testing & Results

* **Testing:** Verified menu routing, empty list states, and accurate currency summation.

## 7. Challenges & Learnings

* **Challenges:** Handling type conversion (`float`/`int`) and volatile runtime memory.
* **Learnings:** Mastered Python loops, dictionaries, lists, and string formatting.

## 8. Future Enhancements

* Integrate JSON/CSV file storage for data persistence and add exception handling.
