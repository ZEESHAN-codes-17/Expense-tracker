def print_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return
    
    print(f"{'ID':<5} {'Date':<12} {'Amount':<10} {'Category':<15} Description")
    print("-" * 60)

    for exp in expenses:
        print(f"{exp['id']:<5} {exp['date']:<12} {exp['amount']:<10} {exp['category']:<15} {exp['description']}")

def pause():
    input("Press Enter to continue...")
        