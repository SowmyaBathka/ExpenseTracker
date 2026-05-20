from data_store import expenses


def add_expense():
    print("\n--- Add Expense ---")

    amount = input("Enter Amount: ")
    category = input("Enter Category: ")
    description = input("Enter Description: ")

    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)

    print("Expense added successfully!")


def view_expenses():
    print("\nView Expenses feature will be implemented later.")