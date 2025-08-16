from storage import init_storage, read_all, write_expense, search_expense, delete_expense
import tkinter as tk
from tkinter import ttk

init_storage()

root = tk.Tk()
root.title("Expense Tracker")
root.geometry("900x650")
root.configure(bg="#1f1f2e")

style = ttk.Style()
style.theme_use('clam')
style.configure("TButton", font=("Arial", 12), padding=8, foreground="#fff", background="#4a90e2")
style.map("TButton", background=[('active', '#357ABD')])

output_frame = tk.Frame(root, bg="#2c2c3a")
output_frame.pack(pady=20, padx=20, fill="both", expand=True)

output_text = tk.Text(output_frame, width=100, height=20, bg="#1e1e2f", fg="#ffffff", font=("Consolas", 11))
output_text.pack(padx=10, pady=10, fill="both", expand=True)

def show_expenses(expenses):
    output_text.delete(1.0, tk.END)
    if not expenses:
        output_text.insert(tk.END, "No expenses found.\n")
        return
    output_text.insert(tk.END, f"{'ID':<5} {'Date':<12} {'Amount':<10} {'Category':<15} Description\n")
    output_text.insert(tk.END, "-"*90 + "\n")
    for exp in expenses:
        output_text.insert(tk.END, f"{exp['id']:<5} {exp['date']:<12} {exp['amount']:<10} {exp['category']:<15} {exp['description']}\n")

def view_all():
    expenses = read_all()
    show_expenses(expenses)

def add_expense_popup():
    popup = tk.Toplevel(root)
    popup.title("Add Expense")
    popup.configure(bg="#2c2c3a")
    popup.geometry("400x350")

    tk.Label(popup, text="Date (YYYY-MM-DD)", bg="#2c2c3a", fg="#ffffff").pack(pady=5)
    date_entry = tk.Entry(popup)
    date_entry.pack(pady=5, fill="x", padx=20)

    tk.Label(popup, text="Amount", bg="#2c2c3a", fg="#ffffff").pack(pady=5)
    amount_entry = tk.Entry(popup)
    amount_entry.pack(pady=5, fill="x", padx=20)

    tk.Label(popup, text="Category", bg="#2c2c3a", fg="#ffffff").pack(pady=5)
    category_entry = tk.Entry(popup)
    category_entry.pack(pady=5, fill="x", padx=20)

    tk.Label(popup, text="Description", bg="#2c2c3a", fg="#ffffff").pack(pady=5)
    description_entry = tk.Entry(popup)
    description_entry.pack(pady=5, fill="x", padx=20)

    def submit():
        write_expense(date_entry.get(), amount_entry.get(), category_entry.get(), description_entry.get())
        popup.destroy()
        view_all()

    ttk.Button(popup, text="Add Expense", command=submit).pack(pady=15)

def search_expense_popup():
    popup = tk.Toplevel(root)
    popup.title("Search Expense")
    popup.configure(bg="#2c2c3a")
    popup.geometry("350x150")

    tk.Label(popup, text="Search term", bg="#2c2c3a", fg="#ffffff").pack(pady=10)
    term_entry = tk.Entry(popup)
    term_entry.pack(pady=5, fill="x", padx=20)

    def submit():
        results = search_expense(term_entry.get())
        show_expenses(results)
        popup.destroy()

    ttk.Button(popup, text="Search", command=submit).pack(pady=15)

def delete_expense_popup():
    popup = tk.Toplevel(root)
    popup.title("Delete Expense")
    popup.configure(bg="#2c2c3a")
    popup.geometry("350x150")

    tk.Label(popup, text="Enter ID to delete", bg="#2c2c3a", fg="#ffffff").pack(pady=10)
    id_entry = tk.Entry(popup)
    id_entry.pack(pady=5, fill="x", padx=20)

    def submit():
        delete_expense(id_entry.get())
        popup.destroy()
        view_all()

    ttk.Button(popup, text="Delete", command=submit).pack(pady=15)

button_frame = tk.Frame(root, bg="#1f1f2e")
button_frame.pack(pady=10)

ttk.Button(button_frame, text="View All Expenses", command=view_all).grid(row=0, column=0, padx=10, pady=5)
ttk.Button(button_frame, text="Add New Expense", command=add_expense_popup).grid(row=0, column=1, padx=10, pady=5)
ttk.Button(button_frame, text="Search Expense", command=search_expense_popup).grid(row=0, column=2, padx=10, pady=5)
ttk.Button(button_frame, text="Delete Expense", command=delete_expense_popup).grid(row=0, column=3, padx=10, pady=5)
ttk.Button(button_frame, text="Exit", command=root.quit).grid(row=0, column=4, padx=10, pady=5)

root.mainloop()

