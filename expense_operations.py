from data_store import expenses
from storage import save_expenses
from validations import validate_amount, validate_text


def add_expense():
    print("\n--- Add Expense ---")

    amount = input("Enter Amount: ")
    category = input("Enter Category: ")
    description = input("Enter Description: ")

    if not validate_amount(amount):
        return 
    
    if not validate_text(category, "Category"):
        return 
    
    if not validate_text(description,"Description"):
        return

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

def total_expenses():
    print("\n---Total Expense Analysis---")

    if len(expenses)==0:
        print("No expenses available.")
        return 
    total=0

    for expense in expenses:
        total+=float(expense["amount"])
    print(f"Total Spending: ₹{total}")

def average_expenses():
    print("\n---Average Expense Analysis---")

    if len(expenses)==0:
        print("No Expenses available.")
        return
     
    total=0

    for expense in expenses:
        total += float(expense["amount"])

    average = total/len(expenses)

    print(f"Average Expense: ₹{average}")

def category_analysis():
    print("\n---Category-wise Expense Analysis---")

    if len(expenses)==0:
        print("No expenses available.")
        return 
    
    category_totals = {}

    for expense in expenses:
        category=expense["category"]
        amount = float(expense["amount"])

        if category in category_totals:
            category_totals[category]+=amount 
        else:
            category_totals[category] = amount 

    print("\nCategory Summary:")

    for category,total in category_totals.items():
        print(f"{category}: ₹{total}")


def search_expenses():
    print("\n--- Search Expenses ---")

    if len(expenses) == 0:
        print("No expenses available.")
        return

    search_value = input("Enter category or description to search: ").strip().lower()

    found = False

    for expense in expenses:
        if (
            expense["category"].lower() == search_value
            or expense["description"].lower() == search_value
        ):
            print("\nMatching Expense:")
            print("Amount     :", expense["amount"])
            print("Category   :", expense["category"])
            print("Description:", expense["description"])
            found = True

    if not found:
        print("No matching expenses found.")