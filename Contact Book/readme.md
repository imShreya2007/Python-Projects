# Contact Book (CSV-Based Console Application)

A **Python console-based Contact Book** that allows users to **add, view, search, edit, and delete contacts**, with all data stored persistently in a **CSV file**. The application includes duplicate detection, input validation, and an intuitive menu-driven interface.

---

## Table of Contents

* [Features](#features)
* [Usage](#usage)
* [Menu Options](#menu-options)
* [How It Works](#how-it-works)
* [Data Storage](#data-storage)
* [Concepts Covered](#concepts-covered)

---

## Features

* Add new contacts with **name, phone number, and email**
* Automatically creates a CSV file on first run
* Prevents duplicate contacts by:
  * Name
  * Phone number
  * Email
* View all contacts sorted alphabetically
* Search contacts using **partial name or phone number**
* Edit existing contacts with partial matching
* Delete contacts with confirmation
* Input validation for:
  * Empty names
  * Invalid phone numbers
  * Incorrect email format
* Persistent data storage using CSV files
* Clean, menu-driven console interface

---

## Usage

1. Run the program:

```bash
python contact_book.py
```
2. Choose an option from the menu.
3. Follow the prompts to manage your contacts.
4. Select **Exit** to close the program safely.

---

## Menu Options

| Option | Description              |
| ------ | ------------------------ |
| 1      | Add a new contact        |
| 2      | View all contacts        |
| 3      | Search contacts          |
| 4      | Edit an existing contact |
| 5      | Delete a contact         |
| 6      | Exit the application     |

---

## How It Works

* Contacts are stored as rows in a CSV file (`contacts.csv`).
* Each contact contains:
  * Name
  * Phone number
  * Email address
* The program:
  * Reads contacts using `csv.DictReader`
  * Writes updates using `csv.DictWriter`
* Duplicate checks are performed before adding or updating contacts.
* Partial matching allows flexible searching, editing, and deletion.
* The entire contact list is rewritten after edits or deletions to maintain consistency.

---

## Data Storage
* File name: `contacts.csv`
* Format:
```
Name,Phone,Email
John Doe,9876543210,john@example.com
Jane Smith,9123456789,jane@email.com
```
* Data persists even after the program exits.

---

## Concepts Covered

* File handling with CSV
* Dictionaries and lists
* Data validation and sanitization
* Searching and filtering data
* Sorting data alphabetically
* Functions and modular programming
* Menu-driven program design
* Exception-safe user input handling

---
