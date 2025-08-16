import os
import csv

def init_storage():
    file_path = 'expenses.csv'
    if os.path.exists(file_path):
        return
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["id", "date", "amount", "category", "description"])

def read_all():
    file_path = 'expenses.csv'
    with open(file_path, 'r', newline='') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]

def write_expense(date, amount, category, description):
    file_path = 'expenses.csv'
    expenses = read_all()
    expense_id = len(expenses) + 1
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([expense_id, date, amount, category, description])

def search_expense(search_term):
    file_path = 'expenses.csv'
    search_term = search_term.lower()
    result = []
    with open(file_path, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if (search_term in row['description'].lower() or
                search_term in row['category'].lower() or
                search_term in row['date'].lower()):
                result.append(row)
    return result

def delete_expense(expense_id):
    file_path = 'expenses.csv'
    expenses = read_all()
    with open(file_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["id", "date", "amount", "category", "description"])
        writer.writeheader()
        for expense in expenses:
            if expense["id"] != str(expense_id):
                writer.writerow(expense)

