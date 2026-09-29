# Design Document — Python Expense Tracker

## 1. Overview

The Python Expense Tracker is a console-based, menu-driven application designed to record and calculate daily expenses. The application uses basic Python data structures and control-flow concepts to provide a simple and interactive expense management system.

---

## 2. Design Goals

The main design goals are:

* Keep the application simple and easy to use.
* Organize expense information clearly.
* Provide a menu-driven interface.
* Allow multiple expenses to be stored during program execution.
* Automatically calculate the total amount spent.
* Apply fundamental Python programming concepts.

---

## 3. System Structure

The application consists of a single main program that controls all operations.

```text
Python Expense Tracker
        |
        v
   Main Menu
        |
   +----+----+----+
   |    |    |    |
   v    v    v    v
 Add  View  Total Exit
      All
    Expenses
```

The program continuously displays the menu until the user selects the Exit option.

---

## 4. Data Design

The application uses a list to store multiple expense records.

```python
expensesLIST = []
```

Each individual expense is represented using a dictionary:

```python
expense = {
    'date': date,
    'category': category,
    'description': description,
    'amount': amount
}
```

### Expense Fields

| Field         | Description                              |
| ------------- | ---------------------------------------- |
| `date`        | Date on which the expense occurred       |
| `category`    | Category of the expense                  |
| `description` | Additional information about the expense |
| `amount`      | Amount spent                             |

The dictionary is added to the list using:

```python
expensesLIST.append(expense)
```

---

## 5. U
