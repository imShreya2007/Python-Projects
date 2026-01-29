print("Hangman Game....")

import random
import time

# RULES 
def show_rules():
    print("\nWELCOME TO HANGMAN ")
    print("\nGAME RULES")
    print("- Guess one letter at a time")
    print("- Each wrong guess costs 1 life")
    print("- Words get harder as you win")
    print("- Faster completion gives higher score")
    print("- You can replay without restarting")
    input("\nPress Enter to start the game...")


#  WORD DATA 
WORD_BANK = {
    1: ["life", "code", "play", "hope"],
    2: ["journey", "python", "future", "coding"],
    3: ["experience", "technology", "developer", "intelligence"]
}


# GET LEVEL SETTINGS 
def get_level_settings(level):
    if level == 1:
        return 6
    elif level == 2:
        return 5
    else:
        return 4


# PLAY ONE ROUND 
def play_game(level):
    lives = get_level_settings(level)
    word = random.choice(WORD_BANK[level])
    guessed_letters = []
    start_time = time.time()

    print(f"\nLEVEL {level}")
    print(f"Word Length: {len(word)} letters")
    print(f"Lives: {lives}")

    while lives > 0:
        display = ""
        for letter in word:
            display += letter if letter in guessed_letters else "_ "

        print("\nWord:", display.strip())
        print(f"Lives left: {lives}")

        if "_" not in display:
            end_time = time.time()
            time_taken = int(end_time - start_time)
            score = (lives * 100) - time_taken
            print("\nYOU WON!")
            print(f"Time Taken: {time_taken}s")
            print(f"Score: {score}")
            return True  # Win

        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Enter a single letter only.")
            continue

        if guess in guessed_letters:
            print("Already guessed.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            lives -= 1
            print("Wrong guess!")

    print("\nGAME OVER")
    print(f"The word was: {word}")
    return False  # Lose


# MAIN PROGRAM 
def main():
    show_rules()

    level = 1

    while True:
        win = play_game(level)

        if win and level < 3:
            level += 1
            print("\n⬆ Difficulty Increased!")
        elif not win:
            level = 1

        replay = input("\nPlay again? (yes/no): ").lower()
        if replay != "yes":
            print("\nThanks for playing!")
            break


# START THE GAME
main()
