# Auction Program

A **Python console-based auction system** that allows multiple bidders to place bids, updates bids for duplicate bidders, validates input, and determines the winner — including handling tie situations.

---

## Table of Contents
- [Features](#features)  
- [Usage](#usage)  
- [How It Works](#how-it-works)  
- [What You’ll Learn](#what-youll-learn)

---

## Features
- Accepts **multiple bidders** with their bid amounts.
- Ensures bids are **valid positive numbers**.  
- Handles **duplicate bidders** by allowing bid updates only if higher.
- Displays a **complete auction summary**.
- Detects and handles **tie situations**.
- README.md Generation Offer

---

## Usage
1. Run the program:
```bash
python auction_program.py
```
2. Enter:
- Bidder name
- Bid amount
3. Choose whether more bidders are participating.
4. View the auction summary and winner(s).

---

## How It Works
1. Uses a dictionary to store bidder names and bids.
2. A dedicated function ensures bid input validation.
3. If a bidder enters their name again:
4. The bid updates only if it is higher than the previous one.
5. The program determines:
- The highest bid
- Whether there is a single winner or a tie
6. Displays all bids before announcing the result.

---

## What You’ll Learn
- Python 3.13.7
- Dictionaries
- Functions
- Loops & conditionals
- Exception handling
- Standard input/output

---

