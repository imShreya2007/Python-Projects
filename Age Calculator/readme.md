# Age to Time Calculator

A **Python console-based application** that calculates a person’s **exact age** and the **total time they have lived** in days, hours, minutes, and seconds. The program validates input, handles leap years correctly, and allows repeated calculations.

---

## Table of Contents

* [Features](#features)
* [Usage](#usage)
* [How It Works](#how-it-works)
* [Output Details](#output-details)
* [Concepts Covered](#concepts-covered)
* [Example](#example)

---

## Features

* Accepts birthdate in `YYYY-MM-DD` format
* Calculates **exact age** in:
  * Years
  * Months
  * Days
* Calculates **total time lived** in:
  * Days
  * Hours
  * Minutes
  * Seconds
* Handles month-length differences and leap years
* Prevents future-date input
* Allows users to repeat calculations
* Clean and user-friendly console output

---

## Usage

1. Run the program:
```bash
python age_to_time.py
```
2. Enter your birthdate in the format:
```
YYYY-MM-DD
```
3. View:
* Your exact age
* Total time lived
4. Choose whether to calculate again or exit.

---

## How It Works

* Uses Python’s `datetime` module to calculate time differences.
* Uses the `calendar` module to correctly determine the number of days in each month.
* Applies a **borrowing system** when:
  * The current day is less than the birth day
  * The current month is less than the birth month
* Converts the total time lived into seconds, minutes, hours, and days.

---

## Concepts Covered

* Date and time manipulation
* Working with `datetime` and `calendar` modules
* Input validation and exception handling
* Arithmetic calculations
* Loop control and program flow
* User-friendly CLI design

---
