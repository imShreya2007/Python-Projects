from datetime import datetime

print("Bill Splitter....")

people_count = int(input("\nHow many people are there in the group? "))

if people_count <= 0:
    print("\nGroup must have at least one person.")
    exit()

names = []
for i in range(people_count):
    name = input(f"\nEnter the name of person #{i+1}: ").strip().title()
    names.append(name)

def get_float(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        print("Invalid number.")
        exit()

try:
    bill = get_float("What was the total bill? ₹")
except ValueError:
    print("Please enter a valid amount.")
    exit()

tip_choice = input("\nWould you like to give tip (Yes/No): ").lower().strip()
total_bill = bill

if tip_choice not in ("yes", "y", "no", "n"):
    print("Invalid choice. Assuming no tip.")

if tip_choice in ("yes", "y"):
    try:
        tip_percent = float(input("\nHow much percent of tip would you like to give? "))
        if tip_percent < 0:
            print("Tip cannot be negative.")
            exit()

    except ValueError:
        print("Please enter a valid tip percentage.")
        exit()
    total_bill += (tip_percent / 100) * bill

split_bill = round(total_bill / people_count, 2)

#DateTime
now = datetime.now()
timestamp = now.strftime("%d %B %Y, %I:%M %p")

#Receipt content
receipt = []
receipt.append("====== BILL SPLIT RECEIPT ======\n")
receipt.append(f"Date & Time: {timestamp}\n")
receipt.append(f"Total Bill: ₹{total_bill:.2f}\n")
receipt.append(f"People Count: {people_count}\n")
receipt.append(f"Each Person Pays: ₹{split_bill:.2f}\n\n")
receipt.append("---- Individual Breakdown ----\n")

print("\n---- Individual Breakdown ----")
for index, name in enumerate(names, start=1):
    line = f"{index}. {name} owes ₹{split_bill:.2f}\n"
    print(line, end="")
    receipt.append(line)

#Save custom name receipt
def save_receipt():
    custom_name = input("\nEnter filename (press Enter for default): ").strip()

    if not custom_name:
        filename = f"bill_receipt_{now.strftime('%Y%m%d_%H%M%S')}.txt"
    else:
        if not custom_name.endswith(".txt"):
            custom_name += ".txt"
        filename = custom_name

    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(receipt)

    print(f"\n✅ Receipt saved as '{filename}'")

#Save reciept choice
save = input("\nDo you want to save the receipt? (Yes/No): ").lower().strip()

if save in ("yes", "y"):
    save_receipt()
else:
    print("\nReceipt not saved.")
    retry = input("Do you want to save it now? (Yes/No): ").lower().strip()
    if retry in ("yes", "y"):
        save_receipt()
    else:
        print("\nExiting without saving the receipt.")
