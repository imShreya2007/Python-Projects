# Secure Calculator 

A **Python console-based calculator** that safely evaluates mathematical expressions using Python’s **Abstract Syntax Tree (AST)**. Unlike traditional calculators that rely on `eval()`, this program **prevents unsafe code execution** by allowing only approved operators.

---

## Table of Contents

* [Features](#features)
* [Usage](#usage)
* [How It Works](#how-it-works)
* [Supported Operations](#supported-operations)
* [Concepts Covered](#concepts-covered)


---

## Features

* Secure evaluation of mathematical expressions
* Prevents execution of unsafe or malicious code
* Supports common arithmetic operators
* Handles parentheses for complex expressions
* Clean error handling for invalid input
* Interactive command-line interface
* Exit command to safely stop the program

---

## Usage

1. Run the program:

```bash
python calculator.py
```

2. Enter a mathematical expression:

```
Enter Your Calculation: (5 + 3) * 2
```

3. View the result instantly.

4. Type `exit` to quit the calculator.

---

## How It Works

1. User input is parsed using Python’s `ast` module.
2. The expression is converted into an Abstract Syntax Tree.
3. Each node is evaluated recursively.
4. Only **allowed operators** are executed using a predefined mapping.
5. Any unsupported syntax or operation raises an error.

This approach avoids the security risks associated with Python’s built-in `eval()`.

---

## Supported Operations

| Operator | Description    |
| -------- | -------------- |
| `+`      | Addition       |
| `-`      | Subtraction    |
| `*`      | Multiplication |
| `/`      | Division       |
| `%`      | Modulus        |
| `**`     | Power          |
| `( )`    | Grouping       |

---

## Concepts Covered

* Abstract Syntax Trees (AST)
* Secure code evaluation
* Dictionaries for operator mapping
* Recursive function calls
* Exception handling
* Input validation
* Command-line interaction

---
