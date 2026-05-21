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
    print("\n---View Expenses---")

    if len(expenses)==0:
        print("No expenses found.")
        return 
    for index, expense in enumerate(expenses,start=1):
        print(f"\nExpense {index}")
        print("Amount :",expense["amount"])
        print("Category :",expense["category"])
        print("Description :",expense["description"])