from utils import add_expense, get_summary, view_all


while True:

    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. Summary")
    print("3. View All")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        category = input("Enter category: ")
        amount = float(input("Enter amount: "))

        add_expense(category, amount)

    elif choice == "2":

        summary = get_summary()

        print("\nExpense Summary")
        print("-" * 30)

        if not summary:
            print("No expenses found.")

        for category, total in summary.items():
            print(f"{category:<15} ₹{total}")

    elif choice == "3":

        view_all()

    elif choice == "4":

        print("Goodbye!")
        break

    else:

        print("Invalid choice.")