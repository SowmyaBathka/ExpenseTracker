from expense_operations import add_expense, view_expenses, delete_expense, total_expenses,  average_expenses, category_analysis, search_expenses

def show_menu():
    print("\n"+"*"*40)
    print("---EXPENSE TRACKER SYSTEM---")
    print("*"*40)
    print("1.Add Expense")
    print("2.View Expense")
    print("3.Delete Expense")
    print("4.Total Spending")
    print("5.Average Spending")
    print("6.Category Analysis")
    print("7.Search Expense")
    print("8.Exit")

def main():
    while True:
        try:
            show_menu()

            choice= input("Enter your choice (1-8):")

            if choice == "1":
                add_expense()
            
            elif choice == "2":
                view_expenses()

            elif choice == "3":
                delete_expense()

            elif choice == "4":
                total_expenses()

            elif choice == "5":
                average_expenses()

            elif choice == "6":
                category_analysis()

            elif choice == "7":
                search_expenses()

            elif choice == "8":
                print("\nThank You for using Expense Tracker!")
                break 

            else:
                print("\nInvalid choice! Please enter a number between 1 and 8.")
        except KeyboardInterrupt:
            print("\nProgram interrupted by user.")
            break

        except Exception as error:
            print("Unexpected error:",error)
            
main()