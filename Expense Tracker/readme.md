# Expense Tracker

A **Python console-based Expense Tracker** that helps users **record, manage, and analyze daily expenses**.  
The application supports **persistent storage using CSV files**, category-wise analysis, searching, monthly summaries, and input validation — making it a practical real-world finance management project.

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

* Add multiple expenses with date, category, description, and amount
* Validates date format (`DD-MM-YYYY`)
* Prevents invalid or negative expense amounts
* View all recorded expenses in a readable format
* Calculate total expenses, Category-wise totals
* Search expenses by category
* Generate monthly expense summaries
*  Persistent data storage using CSV
* Automatically loads existing data on startup
* Saves data safely before exiting
* Simple, menu-driven console interface

---

## Usage

1. Run the program:

```bash
python expense_tracker.py
```
2. Choose an option from the menu by entering the corresponding number.
3. Follow the on-screen instructions to manage your expenses.
4. Select **Exit (7)** to save data and close the program.

---

## Menu Options

| Option | Description                     |
| ------ | ------------------------------- |
| 1      | Add new expense(s)              |
| 2      | View all expenses               |
| 3      | View total expense              |
| 4      | View category-wise totals       |
| 5      | Edit or update an expense       |
| 6      | Delete an expense               |
| 7      | Exit the program                |
| 8      | Search expenses (date/category) |
| 9      | Monthly expense summary         |

---

## How It Works

* Expenses are stored as dictionaries inside a list.
* Each expense contains:

  * Date
  * Category
  * Description
  * Amount
* On startup:
  * Existing data is loaded from expenses.csv
* On exit:
  * All data is written back to the CSV file
* Date validation is performed using datetime.strptime
* Category and monthly summaries are calculated using loops and dictionaries
* The program runs continuously until the user chooses to exit

---

## Data Storage

* File name: expenses.csv
* Format:
```
date,category,description,amount
12-01-2026,Food,Lunch,120.0
15-01-2026,Transport,Bus Pass,450.0
```
*  Data persists across program runs

---

## Concepts Covered

* File handling with CSV (csv.DictReader, csv.DictWriter)
* Persistent data storage
* Dictionaries and lists
* Date validation using datetime
* User input validation
* Conditional logic
* Loop-based menu systems
* Searching and filtering data
* Aggregation (totals & summaries)
* Modular helper functions
* Console-based application design

---
