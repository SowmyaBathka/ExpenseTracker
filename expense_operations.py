from data_store import expenses
from storage import save_expenses


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
    save_expenses(expenses)

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


def delete_expense():
    print("\n---Delete Expense---")

    if len(expenses)==0:
        print("No expenses available to delete.")
        return 
    
    view_expenses()
    expense_number=input("\nEnter Expense number to delete:")

    if not expense_number.isdigit():
        print("Please enter a valid number.")
        return 
    
    expense_number=int(expense_number)

    if expense_number<1 or expense_number >len(expenses):
        print("Expense number out of range.")
        return
    deleted_expense =expenses.pop(expense_number-1)
    save_expenses(expenses)

    print(f"Expense '{deleted_expense['description']}' deleted successfully!")