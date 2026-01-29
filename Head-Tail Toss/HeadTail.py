import random

print("Heads & Tails Game....")

# Statistics
total_tosses = 0
wins = 0
losses = 0

while True:
    # User choice
    choice = input("\nChoose Heads or Tails (h/t): ").strip().lower()
    if choice not in ["h", "t"]:
        print("Invalid choice! Enter 'h' for Heads or 't' for Tails.")
        continue

    user_choice = "heads" if choice == "h" else "tails"

    # Number of tosses
    try:
        toss_count = int(input("How many tosses do you want? "))
        if toss_count <= 0:
            print("Number must be greater than 0.")
            continue
    except ValueError:
        print("Please enter a valid number.")
        continue

    print("\nossing the coin...\n")

    for i in range(1, toss_count + 1):
        coin = random.choice(["heads", "tails"])
        total_tosses += 1

        print(f"Toss {i}: {coin}")

        if coin == user_choice:
            wins += 1
        else:
            losses += 1

    # Show statistics
    print("\nGame Statistics")
    print("--------------------")
    print(f"Total Tosses : {total_tosses}")
    print(f"Wins         : {wins}")
    print(f"Losses       : {losses}")

    win_rate = (wins / total_tosses) * 100
    print(f"Win Rate     : {win_rate:.2f}%")

    # Play again?
    again = input("\nPlay again? (yes/no): ").strip().lower()
    if again != "yes":
        print("\nThanks for playing!")
        break
