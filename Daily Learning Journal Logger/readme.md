# Daily Learning Journal Logger

A **Python console application** that helps you log what you learn every day. Each entry is saved with a **timestamp, category, optional productivity rating**, and stored in a text file for long-term tracking.

---

## Table of Contents
- [Features](#features)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [What You’ll Learn](#what-youll-learn)

---

## Features
- Logs daily learning entries interactively.
- Prevents empty journal entries.
- Allows categorization (Python, DSA, AI, College, etc.).
- Optional **productivity rating (1–5)** with validation.
- Automatically adds **date & time** to each entry.
- Appends entries to a persistent `learning_journal.txt` file.
- Allows multiple entries in one session.

---

## Usage

1. Run the program:
```bash
python daily_learning_journal.py
```
Enter:
- What you learned today
- Learning category
- Optional productivity rating (1–5)
3. Preview the journal entry.
4. Confirm whether to save it.
5. Choose to add another entry or exit.

---

## How It Works
1. Uses a while loop to allow multiple journal entries in one run.
2. Validates:
- Non-empty learning input
- Productivity rating between 1 and 5
3. Uses the datetime module to generate timestamps.
4. Formats journal entries using multi-line strings.
5. Appends entries to a .txt file without overwriting previous logs.

---

## What You’ll Learn
- Working with loops and conditionals
- Input validation techniques
- Using the datetime module
- File handling with append mode
- String formatting and multi-line text
- Building real-world console utilities

