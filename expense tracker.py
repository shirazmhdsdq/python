import json
import os
from datetime import datetime

DATA_FILE = 'expenses.json'


def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)


def save_expenses(expenses):
    with open(DATA_FILE, 'w') as f:
        json.dump(expenses, f, indent=4)


def add_expense():
    amount = float(input("Enter amount: ₹ "))
    category = input("Enter category (e.g., Food, Travel, Bills): ").strip()
    description = input("Enter description: ").strip()
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    expense = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
    }

    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)
    print("✅ Expense added!\n")


def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded yet.\n")
        return

    print("\n📋 All Expenses:")
    for idx, exp in enumerate(expenses, start=1):
        print(f"{idx}. ₹{exp['amount']} - {exp['category']} - {exp['description']} ({exp['date']})")
    print()


def expense_summary():
    expenses = load_expenses()
    if not expenses:
        print("No expenses to summarize.\n")
        return

    total = 0
    category_totals = {}

    for exp in expenses:
        total += exp["amount"]
        cat = exp["category"]
        category_totals[cat] = category_totals.get(cat, 0) + exp["amount"]

    print("\n💰 Expense Summary:")
    print(f"Total spent: ₹{total:.2f}")
    print("By category:")
    for cat, amt in category_totals.items():
        print(f"  - {cat}: ₹{amt:.2f}")
    print()


def main():
    while True:
        print("📌 Expense Tracker Menu")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Expense Summary")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            expense_summary()
        elif choice == '4':
            print("👋 Exiting. Bye!")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()

