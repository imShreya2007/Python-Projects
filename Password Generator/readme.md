# Password Generator and Strength Checker

A **Python console application** that allows users to **check the strength of a password** or **generate a secure random password** based on customizable criteria. Designed with security best practices in mind.

---

## Table of Contents
- [Features](#features)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [What You’ll Learn](#what-youll-learn)

---

## Features
- Checks password strength against common security rules.
- Identifies missing requirements and provides clear feedback.
- Generates secure random passwords.
- Allows users to customize:
  - Number of letters
  - Numbers
  - Special characters
- Hides password input during strength checking.
- Simple and interactive console interface.

---

## Usage

1. Run the program:
```bash
python password_generator.py
````
2. Choose an option:
- 1 → Check password strength
- 2 → Generate a password
3. Follow the on-screen prompts.

---

## How It Works

1. Password Strength Checking
Uses a function to validate:
- Minimum length (8 characters)
- Lowercase letters
- Uppercase letters
- Numbers
- Special characters
Displays all issues if the password is weak.
Uses the getpass module to hide password input for security.

2. Password Generation
- Uses the random and string modules.
- Randomly selects letters, numbers, and symbols.
- Shuffles characters to improve randomness.
- Generates a strong password based on user-defined counts.

--- 

## What You’ll Learn
- Password security fundamentals
- Input validation techniques
- Working with Python’s random module
- Using the string module for character sets
- Secure input handling with getpass
- Writing modular and reusable functions
