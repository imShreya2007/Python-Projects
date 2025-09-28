import random
print("Number Guessing Game.")
numbers = list(range(1, 101))
random_number = random.choice(numbers)
user_input = None
while user_input != random_number:
    user_input = int(input("Guess a number between 1 to 100: "))
    if user_input == random_number:
        print("You Win")
    else:
        print("You lose.Try Again")