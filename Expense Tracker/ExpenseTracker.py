from datetime import datetime
import csv
import os

print("Expense Tracker....")

FILENAME = "expenses.csv"

# Helper Functions 

def is_valid_date(date):
    try:
        datetime.strptime(date, "%d-%m-%Y")
        return True
    except ValueError:
        return False


def load_expenses():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [
            {
                "date": row["date"],
                "category": row["category"],
                "description": row["description"],
                "amount": float(row["amount"])
            }
            for row in reader
        ]


def save_expenses(expenses):
    with open(FILENAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["date", "category", "description", "amount"]
        )
        writer.writeheader()
        writer.writerows(expenses)


# Load Existing Data 
expenses_list = load_expenses()

# Main Loop 
while True:
    print("\n----- Menu -----")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expense")
    print("4. View Category-wise Total")
    print("5. Edit Expense")
    print("6. Delete Expense")
    print("7. Exit")
    print("8. Search Expenses")
    print("9. Monthly Summary")

    choice = input("Enter your choice: ").strip()

    # ADD EXPENSE
    if choice == "1":
        date = input("Enter Date (DD-MM-YYYY): ").strip()
        if not is_valid_date(date):
            print("Invalid date format.")
            continue

        category = input("Enter Category: ").strip().title()
        description = input("Enter Description: ").strip()

        try:
            amount = float(input("Enter Amount: "))
            if amount <= 0:
                raise ValueError
        except ValueError:
            print("Invalid amount.")
            continue

        expenses_list.append({
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        })

        print("Expense added successfully!")

    # VIEW ALL
    elif choice == "2":
        if not expenses_list:
            print("No expenses found.")
        for i, exp in enumerate(expenses_list, 1):
            print(f"{i}. {exp}")

    # TOTAL
    elif choice == "3":
        print(f"Total Expense: ₹{sum(e['amount'] for e in expenses_list)}")

    # CATEGORY TOTAL
    elif choice == "4":
        totals = {}
        for e in expenses_list:
            totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]
        for k, v in totals.items():
            print(f"{k}: ₹{v}")

    # SEARCH
    elif choice == "8":
        cat = input("Enter category: ").strip().title()
        matches = [e for e in expenses_list if e["category"] == cat]
        print(matches if matches else "No results found.")

    # MONTHLY SUMMARY
    elif choice == "9":
        month = input("Month (MM): ")
        year = input("Year (YYYY): ")

        total = 0
        for e in expenses_list:
            d, m, y = e["date"].split("-")
            if m == month and y == year:
                total += e["amount"]

        print(f"Total for {month}-{year}: ₹{total}")

    # EXIT
    elif choice == "7":
        save_expenses(expenses_list)
        print("Data saved. Goodbye!")
        break

    else:
        print("Invalid choice.")
