import json

FILE_NAME = "expenses.json"


def load_expenses():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_expenses(expenses):
    with open(FILE_NAME, "w") as f:
        json.dump(expenses, f, indent=2)


def add_expense(category, amount):

    expenses = load_expenses()

    expense = {
        "category": category,
        "amount": amount
    }

    expenses.append(expense)

    save_expenses(expenses)

    print("Expense added successfully.")


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

    for expense in expenses:
        print(
            f"Category: {expense['category']:<15}"
            f"Amount: ₹{expense['amount']}"
        )