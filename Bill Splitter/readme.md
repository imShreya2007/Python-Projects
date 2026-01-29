# Bill Splitter Program

A **Python console application** that helps groups split bills fairly, including optional tips. The program generates an **individual breakdown**, calculates the tip, and can save a **receipt with a timestamp**.

---

## Table of Contents
- [Features](#features)  
- [Usage](#usage)  
- [How It Works](#how-it-works)  
- [What You’ll Learn](#what-youll-learn)  

---

## Features
- Accepts any number of people in a group.  
- Allows users to input the **total bill** and **tip percentage**.  
- Calculates **individual share** with tip included.  
- Displays a detailed **individual breakdown**.  
- Optionally saves a **receipt as a text file** with date & time.  
- Validates user input to avoid errors.  

---

## Usage
- Run the program:
```bash
python bill_splitter.py
```
- Enter the number of people in the group.
- Enter each person’s name.
- Enter the total bill amount.
- Optionally, provide a tip percentage.
- The program calculates and prints each person’s share.
- You can save the receipt as a .txt file with a custom filename or default timestamped filename.

---

## How It Works
- The program uses Python lists and loops to store people’s names.
- The total bill and optional tip are calculated using basic arithmetic.
- The program rounds each person’s share to 2 decimal places.
- The receipt is generated as a list of strings and optionally written to a text file.
- Timestamps are created using the datetime module to track when the bill was split.

---

## What You’ll Learn
- Python  3.13.7 
- Built-in modules: datetime for timestamps
- Standard I/O 

---