import csv
from datetime import datetime

# File to store the expensesgit remote add origin https://github.com/Vaishnavi-gif-jpg/simple-expense-tracker-python-project.git
EXPENSES_FILE = 'expenses.csv'
# Function to add an expense
def add_expense(amount, category, description=""):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(EXPENSES_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, description])
    print("Expense added successfully.")

# Function to view all expenses
def view_expenses():
    try:
        with open(EXPENSES_FILE, mode='r') as file:
            reader = csv.reader(file)
            print(f"{'Date':<20} {'Amount':<10} {'Category':<15} {'Description':<20}")
            for row in reader:
                print(f"{row[0]:<20} {row[1]:<10} {row[2]:<15} {row[3]:<20}")
    except FileNotFoundError:
        print("No expenses recorded yet.")

# Function to view total expenses
def view_total_expenses():
    total = 0
    try:
        with open(EXPENSES_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                total += float(row[1])
        print(f"Total expenses: ${total:.2f}")
    except FileNotFoundError:
        print("No expenses recorded yet.")

# Main menu
def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Expenses")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            try:
                amount = float(input("Enter the expense amount: "))
            except ValueError:
                print("Please enter a valid number.")
                continue
            category = input("Enter the category (e.g., Food, Transport, Rent): ")
            description = input("Enter a description (optional): ")
            add_expense(amount, category, description)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            view_total_expenses()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if '_name_' == '_main_':
    main()