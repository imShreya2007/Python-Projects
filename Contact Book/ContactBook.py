import csv
import os

print("Contact Book....")

FILENAME = "contacts.csv"

if not os.path.exists(FILENAME):
    with open(FILENAME, mode='w', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([f"Name" , "Phone" , "Email"]) 

def contact_exists(name, phone, email, ignore_name=None):
    with open(FILENAME, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if ignore_name and row["Name"].lower() == ignore_name.lower():
                continue

            if row["Name"].lower() == name.lower():
                return "Name"
            if phone and row["Phone"] == phone:
                return "Phone number"
            if email and row["Email"].lower() == email.lower():
                return "Email"
    return None

def add_contact():
    name = input("Enter name: ").strip().title()
    if not name:
        print("Name cannot be empty.")
        return

    phone = input("Enter phone number: ").strip()
    if phone and not phone.isdigit():
        print("Phone number must contain only digits.")
        return

    email = input("Enter email address: ").strip().lower()
    if email and "@" not in email:
        print("Invalid email format.")
        return

    duplicate = contact_exists(name, phone, email)
    if duplicate:
        print(f"Contact with this {duplicate} already exists.")
        return

    with open(FILENAME, mode='a', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([name, phone, email])

    print("Contact added successfully.")

def view_contacts():
    with open(FILENAME, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        contacts = list(csv_reader)
        if not contacts:
            print("No contacts found.")
            return
        
        # Sort contacts alphabetically by Name
        contacts.sort(key=lambda x: x["Name"].lower())
        
        print("Your Contacts:")
        for contact in contacts:
            print(f"Name: {contact['Name']} | Phone: {contact['Phone']} | Email: {contact['Email']}")
        print(f"Total contacts: {len(contacts)}\n")

def search_contact():
    search_term = input("Enter name or phone to search: ").strip().lower()
    found_contacts = []

    with open(FILENAME, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if (search_term in row["Name"].lower() or
                search_term in row["Phone"]):
                found_contacts.append(row)

    if found_contacts:
        print("\nContacts Found:")
        for contact in found_contacts:
            print(f"{contact['Name']} | Phone: {contact['Phone']} | Email: {contact['Email']}")
        print(f"Total matches: {len(found_contacts)}\n")
    else:
        print("No contacts found.")


def edit_contact():
    search_term = input("Enter name of the contact to edit (partial name allowed): ").strip().lower()
    contacts = []
    found_contacts = []

    # Load all contacts
    with open(FILENAME, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            contacts.append(row)
            if search_term in row["Name"].lower():
                found_contacts.append(row)

    if not found_contacts:
        print("No contacts found matching that name.")
        return

    # Show matches
    print("Matching contacts:")
    for i, contact in enumerate(found_contacts, start=1):
        print(f"{i}. {contact['Name']} | Phone: {contact['Phone']} | Email: {contact['Email']}")

    # Let user choose
    choice = input(f"Enter the number of the contact to edit (1-{len(found_contacts)}): ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(found_contacts)):
        print("Invalid selection.")
        return

    selected = found_contacts[int(choice)-1]

    print("Enter new details (leave blank to keep current value):")
    new_name = input(f"New name [{selected['Name']}]: ").strip().title() or selected["Name"]
    if not new_name:
        print("Name cannot be empty.")
        return
    new_phone = input(f"New phone [{selected['Phone']}]: ").strip() or selected["Phone"]
    if new_phone and not new_phone.isdigit():
        print("Phone number must contain only digits.")
        return
    new_email = input(f"New email [{selected['Email']}]: ").strip().lower() or selected["Email"]
    if new_email and "@" not in new_email:
        print("Invalid email format.")
        return

    duplicate = contact_exists(
    new_name,
    new_phone,
    new_email,
    ignore_name=selected["Name"])
    if duplicate:
        print(f"Cannot update. Contact with this {duplicate} already exists.")
        return


    # Update contact in the main list
    for contact in contacts:
        if contact == selected:
            contact["Name"] = new_name
            contact["Phone"] = new_phone
            contact["Email"] = new_email
            break

    # Write back to CSV
    with open(FILENAME, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ["Name", "Phone", "Email"]
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(contacts)

    print("Contact updated successfully.")

def delete_contact():
    search_term = input("Enter name of the contact to delete (partial name allowed): ").strip().lower()
    contacts = []
    found_contacts = []

    with open(FILENAME, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            contacts.append(row)
            if search_term in row["Name"].lower():
                found_contacts.append(row)

    if not found_contacts:
        print("No contacts found matching that name.")
        return

    print("Matching contacts:")
    for i, contact in enumerate(found_contacts, start=1):
        print(f"{i}. {contact['Name']} | Phone: {contact['Phone']} | Email: {contact['Email']}")

    choice = input(f"Enter the number of the contact to delete (1-{len(found_contacts)}): ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(found_contacts)):
        print("Invalid selection.")
        return

    selected = found_contacts[int(choice) - 1]

    confirmation = input("Are you sure you want to delete this contact? (yes/no): ").lower()
    if confirmation != "yes":
        print("Delete cancelled.")
        return

    contacts = [contact for contact in contacts if contact != selected]

    with open(FILENAME, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ["Name", "Phone", "Email"]
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(contacts)

    print("Contact deleted successfully.")


def main():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Edit Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            edit_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
