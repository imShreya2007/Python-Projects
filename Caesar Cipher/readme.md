## Caesar Cipher Program

A Python console-based Caesar Cipher application that allows users to encrypt (encode) and decrypt (decode) text using a shift-based substitution cipher. The program supports both uppercase and lowercase letters while preserving non-alphabetic characters.

---

## Table of Contents
- [Features](#features)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [What You’ll Learn](#what-youll-learn)

---

## Features
- Encrypts and decrypts text using the Caesar Cipher technique
- Supports uppercase and lowercase letters
- Preserves spaces, numbers, and special characters
- Handles large shift values using modulo logic
- Interactive loop to perform multiple operations
- Clean and beginner-friendly console interface

---

## Usage

1.Run the program:
```bash
python caesar_cipher.py
```
2. Choose an option:
- encode → Encrypt a message
- decode → Decrypt a message
3. Enter:
- The message
- The shift number
4. View the result and choose whether to continue.

---

## How It Works

1. Uses Python’s string module to access:
- ascii_lowercase
- ascii_uppercase
2. Each letter is shifted forward or backward based on the chosen operation.
3. For decoding, the shift value is reversed automatically.
4. Modulo (% 26) ensures wrapping from z → a and Z → A.
5. Characters that are not letters remain unchanged.

## What You’ll Learn
- Caesar Cipher encryption logic
- String manipulation
- Functions and parameters
- Loops and conditionals
- Modular arithmetic
- Input validation
- Python standard library (string module)