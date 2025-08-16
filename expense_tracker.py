from storage import init_storage, read_all, write_expense, search_expense, delete_expense
from utils import print_expenses, pause

init_storage()

while True:
    print("\nExpense Tracker")
    print("1. View all expenses")
    print("2. Add new expense")
    print("3. Search expense")
    print("4. Delete expense")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        expenses = read_all()
        print_expenses(expenses)
        pause()

    elif choice == "2":
        write_expense()
        print("Expense added successfully.")
        pause()

    elif choice == "3":
        results = search_expense()
        print_expenses(results)
        pause()

    elif choice == "4":
        delete_expense()
        print("Expense deleted successfully.")
        pause()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
        pause()
