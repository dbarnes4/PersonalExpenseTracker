import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt
from collections import defaultdict

# File to store expenses
FILE_PATH = 'expenses.csv'

# Function to initialize the CSV file if it doesn’t exist
def initialize_file():
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Category', 'Amount'])

# Function to check date format
def get_valid_date():
    while True:
        date_str = input("Enter date (YYYY-MM-DD): ")
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d')
            return date_str  
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

# Function to log an expense
def log_expense(date, category, amount):
    with open(FILE_PATH, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])
    print(f"Logged: {amount} in {category} on {date}")

# Function to read expenses from the CSV file
def read_expenses():
    expenses = []
    with open(FILE_PATH, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['Amount'] = float(row['Amount'])
            expenses.append(row)
    return expenses

# Function to calculate total expenses per category
def calculate_totals_by_category(expenses):
    totals = {}
    for expense in expenses:
        category = expense['Category']
        amount = expense['Amount']
        totals[category] = totals.get(category, 0) + amount
    return totals

# Function to visualize expenses by category
def plot_expenses_by_category(totals):
    categories = list(totals.keys())
    amounts = list(totals.values())
    plt.figure(figsize=(10, 6))
    plt.bar(categories, amounts, color='skyblue')
    plt.xlabel('Category')
    plt.ylabel('Total Expense')
    plt.title('Expenses by Category')
    plt.show()

# Function to calculate monthly totals for expenses
def calculate_monthly_totals(expenses):
    monthly_totals = defaultdict(float)
    for expense in expenses:
        date = datetime.strptime(expense['Date'], '%Y-%m-%d')
        month = date.strftime('%Y-%m') 
        monthly_totals[month] += expense['Amount']
    return monthly_totals

# Function to visualize expense trend by month
def plot_expense_trend_monthly(expenses):
    monthly_totals = calculate_monthly_totals(expenses)
    months = list(monthly_totals.keys())
    amounts = list(monthly_totals.values())
    plt.figure(figsize=(10, 6))
    plt.plot(months, amounts, marker='o', color='purple')
    plt.xlabel('Month')
    plt.ylabel('Total Expense')
    plt.title('Expense Trend by Month')
    plt.xticks(rotation=45, ha='right')  
    plt.tight_layout()
    plt.show()

# Main program
initialize_file()

# Loop to keep program running and menu options
while True:
    print("\n--- Expense Tracker ---")
    print("1. Log an Expense")
    print("2. View Total Expenses by Category")
    print("3. View Expense Trend by Month")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        date = get_valid_date()  
        category = input("Enter category (e.g., Food, Transport): ")
        amount = float(input("Enter amount: "))
        log_expense(date, category, amount)

    elif choice == '2':
        expenses = read_expenses()
        totals = calculate_totals_by_category(expenses)
        plot_expenses_by_category(totals)

    elif choice == '3':
        expenses = read_expenses()
        plot_expense_trend_monthly(expenses)  

    elif choice == '4':
        print("Exiting the Expense Tracker.")
        break

    else:
        print("Invalid choice. Please choose again.")
4