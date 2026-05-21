from expense_operations import add_expense, view_expenses, delete_expense

def show_menu():
    print("\n"+"*"*40)
    print("---EXPENSE TRACKER SYSTEM---")
    print("*"*40)
    print("1.Add Expense")
    print("2.View Expense")
    print("3.Delete Expense")
    print("4.Exit")

def main():
    while True:
        show_menu()

        choice= input("Enter your choice (1-4):")

        if choice == "1":
            add_expense()
        
        elif choice == "2":
            view_expenses()

        elif choice == "3":
            delete_expense()

        elif choice == "4":
            print("\nThank You for using Expense Tracker!")
            break 

        else:
            print("\nInvalid choice! Please enter a number between 1 and 4.")
            
main()