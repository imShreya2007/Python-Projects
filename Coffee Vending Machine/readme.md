## Coffee Machine Program

A Python console-based coffee machine simulation that mimics the working of a real coffee vending machine. The program manages resources, processes payments, checks availability, and serves drinks while maintaining a running report.

---
 
## Table of Contents
- [Features](#features)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Available Drinks](#available-drinks)
- [What You’ll Learn](#what-youll-learn)

---

## Features
- Offers three drinks: espresso, latte, cappuccino
- Tracks machine resources (water, milk, coffee)
- Validates resource availability before serving
- Accepts coin-based payments
- Calculates and returns change if applicable
- Maintains total money earned
- Provides a report mode for machine status
- Allows safe shutdown using the off command

---

## Usage
1.Run the program:
```bash
python coffee_machine.py
```
2.Choose an option:
- espresso
- latte
- cappuccino
- report → View available resources
- off → Turn off the machine
3. Insert coins when prompted.
4. Enjoy your coffee if the transaction is successful!

---

## How It Works
1. Menu & Resources
- Drinks and ingredients are stored using dictionaries.
- Resources are updated dynamically after each order.
2.Resource Check
- Ensures enough ingredients are available before processing payment.
3. Coin Processing
- Accepts quarters, dimes, nickels, and pennies.
- Calculates total inserted amount.
3. Transaction Validation
- Confirms sufficient payment.
- Returns change if extra money is inserted.
- Updates machine balance.
4. Coffee Preparation
- Deducts required ingredients.
- Displays confirmation message.

---

## Available Drinks

| Drink	      | Water (ml) | Milk (ml) | Coffee (g) | Cost ($)|
|------------ |------------|-----------|------------|---------|
| Espresso	  |  50	       |  0	       |  18	    |  1.5    |
| Latte       |  200	   |  150	   |  24	    |  2.5    |
| Cappuccino  |  250       |  100	   |  24	    |  3.0    |

---

## What You’ll Learn
- Dictionaries & nested data structures
- Functions and modular programming
- Loops and conditional logic
- Input validation
- Resource management
- Simulating real-world systems
- Basic financial calculations