print("BMI Calculator....")

def bmi_calculator():
    try:
        weight = float(input("Enter your weight (kg): "))
        height = float(input("Enter your height (meters): "))

        if weight <= 0 or height <= 0:
            print("Weight and height must be positive values.")
            return

        bmi = round(weight / (height ** 2), 2)

        print(f"\nYour BMI is: {bmi}")

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        print(f"Category: {category}")

    except ValueError:
        print("Please enter valid numeric values.")


while True:
    bmi_calculator()
    again = input("\nDo you want to calculate again? (yes/no): ").lower()
    if again not in ("yes", "y"):
        print("Goodbye!")
        break
