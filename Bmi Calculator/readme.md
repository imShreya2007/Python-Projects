## BMI Calculator (Console-Based Python Application)

A Python console-based BMI (Body Mass Index) Calculator that allows users to calculate their BMI based on weight and height, determine their health category, and repeat calculations without restarting the program. The application includes input validation and a user-friendly loop-based design.

## Table of Contents 
* [Features](#features)
* [Usage](#usage)
* [How It Works](#how-it-works)
* [BMI Categories](#bmi-categories)
* [Concepts Covered](#concepts-covered)

---

## Features
1. Calculates BMI using weight (kg) and height (meters)
2. Displays BMI value rounded to two decimal places
3. Categorizes BMI into standard health groups:
* Underweight
* Normal weight
* Overweight
* Obese
4. Handles invalid inputs gracefully
5. Prevents negative or zero values for height and weight
6. Allows repeated calculations in a single run
7. Simple and clean console interaction

---

## Usage
1. Run the program:
```bash
python bmi_calculator.py
```
2. Enter:
* Weight in kilograms
* Height in meters
3. View your BMI value and category.

4. Choose whether to calculate again or exit.

---

## How It Works
1. The program:

* Takes user input for weight and height
* Validates numeric and positive input
* Applies the BMI formula:
```
BMI = weight / (height²)
```
2. The calculated BMI is rounded to two decimal places.
3. Based on BMI value, the program determines the health category.
4. A loop allows the user to perform multiple calculations until they choose to exit.
5. Errors such as invalid input types are handled using try-except.

---

## BMI Categories

| BMI Range	     | Category      |
|----------------|---------------|
| Less than 18.5 |Underweight    |
| 18.5 – 24.9	 | Normal weight |
| 25 – 29.9	     | Overweight    |
| 30 and above	 | Obese         |

---

## Concepts Covered
* User input handling
* Type conversion (float)
* Mathematical calculations
* Conditional statements (if-elif-else)
* Exception handling (try-except)
* Infinite loops with controlled exit
* Modular function design
* Console-based user interaction

---
