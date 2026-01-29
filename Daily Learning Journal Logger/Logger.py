from datetime import datetime

print("\nDaily Learning Journal Logger....")

while True:
    learning_journal = input("\nWhat did you learn today?\n> ").strip()
    if not learning_journal:
        print("Journal entry cannot be empty.")
        continue

    category = input("\nAdd learning Category (Python / DSA / AI / College / Other): ").strip().title()
    if not category:
        category = "General"

    rating = input("\nRate your productivity today (1-5) or press Enter to skip: ").strip()
    if rating:
        if not rating.isdigit() or not (1 <= int(rating) <= 5):
            print("Invalid rating. Rating must be between 1 and 5.")
            continue

    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d | %I:%M %p")

    journal_entry = f"""
Date & Time: {date_str}
Category: {category}

What I Learned:
{learning_journal}
"""

    if rating:
        journal_entry += f"\nProductivity Rating: {rating}/5"

    journal_entry += "\n" + "-"*40 + "\n"

    print("\nPreview:")
    print(journal_entry)

    confirm = input("Save this entry? (yes/no): ").lower().strip()
    if confirm == "yes":
        with open("learning_journal.txt", "a", encoding="utf-8") as file:
            file.write(journal_entry)
        print("Entry saved successfully!")
    else:
        print("Entry not saved.")

    again = input("\nAdd another entry? (yes/no): ").lower().strip()
    if again not in ("yes", "y"):
        print("\nJournal session ended. Keep learning!")
        break
