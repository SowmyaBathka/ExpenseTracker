# Expense Tracker

A simple command-line Expense Tracker application built using Python.

This project helps users track daily expenses, analyze spending habits, and manage expense records efficiently using persistent JSON storage.

---

## Features

- Add new expenses
- View all expenses
- Delete expenses
- Search expenses by category or description
- Calculate total spending
- Calculate average spending
- Category-wise expense analysis
- Input validation
- Exception handling
- Persistent JSON storage

---

## Technologies Used

- Python 3
- JSON File Storage
- VS Code
- Git & GitHub

---

## Project Structure

```text
ExpenseTracker/
├── main.py
├── expense_operations.py
├── data_store.py
├── storage.py
├── validations.py
├── expenses.json
└── README.md
```

---

## Module Description

### main.py

Handles:
- main menu
- user interaction
- application flow
- exception handling

---

### expense_operations.py

Handles:
- add expense
- view expenses
- delete expense
- search expenses
- total spending analysis
- average spending analysis
- category analysis

---

### data_store.py

Handles:
- loading expense list into memory

---

### storage.py

Handles:
- saving expenses into JSON file
- loading expenses from JSON file
- file error handling

---

### validations.py

Handles:
- amount validation
- empty text validation

---

## How to Run

### Clone Repository

```bash
git clone https://github.com/SowmyaBathka/ExpenseTracker
```


---

### Move into Project Folder

```bash
cd ExpenseTracker
```

---

### Run Application

```bash
python main.py
```

---

## Sample Menu

```text
=============================================
         EXPENSE TRACKER SYSTEM
=============================================
1. Add Expense
2. View Expenses
3. Delete Expense
4. Total Spending
5. Average Spending
6. Category Analysis
7. Search Expense
8. Exit
```

---

## Example Expense Data

```json
[
    {
        "amount": "250",
        "category": "Food",
        "description": "Lunch"
    },
    {
        "amount": "500",
        "category": "Travel",
        "description": "Bus Pass"
    }
]
```

---

## Future Improvements

Possible enhancements:

- Update expense feature
- Export expense reports
- Monthly spending summary
- GUI version using Tkinter
- SQLite database integration
- User login system

---

## Author

Bathka Sowmya