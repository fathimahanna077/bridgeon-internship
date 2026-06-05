import json
import os

FILE_NAME = "expenses.json"


def load_expenses():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(category, amount):
    expenses = load_expenses()

    expense = {
        "category": category,
        "amount": amount
    }

    expenses.append(expense)

    save_expenses(expenses)

    print("Expense added successfully!")


def get_summary():
    expenses = load_expenses()

    summary = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount

    return summary


def view_all():
    expenses = load_expenses()

    if not expenses:
        print("No expenses found.")
        return

    print("\nAll Expenses")
    print("-" * 30)

    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. Category: {expense['category']} | Amount: ₹{expense['amount']}"
        )