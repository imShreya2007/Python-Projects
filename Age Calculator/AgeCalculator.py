import calendar
from datetime import datetime

print("Age To Time Calculator....")

while True:
    try:
        dob = input("Enter your birthdate (YYYY-MM-DD): ").strip()
        birth_date = datetime.strptime(dob, "%Y-%m-%d")
        now = datetime.now()

        if birth_date > now:
            print("Birthdate cannot be in the future.")
            continue

        # Total time lived
        time_difference = now - birth_date
        total_seconds = int(time_difference.total_seconds())
        total_minutes = total_seconds // 60
        total_hours = total_minutes // 60
        total_days = time_difference.days

        # Exact age
        years = now.year - birth_date.year
        months = now.month - birth_date.month
        days = now.day - birth_date.day

        # Borrow days
        if days < 0:
            months -= 1
            prev_month = now.month - 1 or 12
            prev_year = now.year if now.month != 1 else now.year - 1
            days += calendar.monthrange(prev_year, prev_month)[1]
        # Borrow months
        if months < 0:
            years -= 1
            months += 12

        print("\nYour Exact Age:")
        print(f"{years} years, {months} months, {days} days")

        print("\nTime You Have Lived:")
        print(f"{total_days:,} days")
        print(f"{total_hours:,} hours")
        print(f"{total_minutes:,} minutes")
        print(f"{total_seconds:,} seconds")

        again = input("\nWould you like to try again? (yes/no): ").lower().strip()
        if again in ("no", "n"):
            print("Goodbye!")
            break

    except ValueError as e:
        print("Error:", e)