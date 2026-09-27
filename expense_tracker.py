import csv
import os
from datetime import date


FILE_NAME = "expenses.csv"


def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])


def add_expense():
    print("\n--- Add Expense ---")

    category = input("Enter category: ")
    description = input("Enter description: ")

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Please enter a valid amount.")
        return

    today = date.today()

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([today, category, description, amount])

    print("Expense added successfully!")


def view_expenses():
    print("\n--- All Expenses ---")

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        found = False

        for row in reader:
            found = True
            print(
                f"{row['Date']} | "
                f"{row['Category']} | "
                f"{row['Description']} | "
                f"Rs. {row['Amount']}"
            )

        if not found:
            print("No expenses recorded yet.")


def filter_category():
    print("\n--- Filter Expenses ---")

    category = input("Enter category to search: ")

    found = False

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["Category"].lower() == category.lower():
                found = True

                print(
                    f"{row['Date']} | "
                    f"{row['Description']} | "
                    f"Rs. {row['Amount']}"
                )

    if not found:
        print("No expenses found for this category.")


def category_summary():
    print("\n--- Category Summary ---")

    summary = {}

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])

            if category in summary:
                summary[category] += amount
            else:
                summary[category] = amount

    if not summary:
        print("No expenses recorded yet.")
        return

    for category, total in summary.items():
        print(f"{category}: Rs. {total:.2f}")


def main():
    create_file()

    while True:
        print("\n========================================")
        print("       PERSONAL EXPENSE TRACKER")
        print("========================================")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter by Category")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            filter_category()

        elif choice == "4":
            category_summary()

        elif choice == "5":
            print("\nThank you for using Personal Expense Tracker!")
            break

        else:
            print("Invalid choice. Please enter 1 to 5.")


if __name__ == "__main__":
    main()