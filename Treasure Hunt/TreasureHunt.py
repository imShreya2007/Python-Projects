def treasure_island():
    print("Treasure Hunt")
    print("\nWelcome to Treasure Island.")
    print("Your mission is to find the treasure.\n")

    direction = input(
        "You're at a crossroad. Where do you want to go?\n"
        "Type 'left' or 'right': "
    ).strip().lower()

    if direction == "left":
        action = input(
            "\nYou've come to a lake. There is an island in the middle of the lake.\n"
            "Type 'wait' to wait for a boat.\n"
            "Type 'swim' to swim across: "
        ).strip().lower()

        if action == "wait":
            door = input(
                "\nYou arrive at the island unharmed.\n"
                "There is a house with 3 doors:\n"
                "Red, Yellow, Blue\n"
                "Which color do you choose? "
            ).strip().lower()

            if door == "red":
                print("\nIt's a room full of fire.")
                print("GAME OVER!")
            elif door == "blue":
                print("\nYou enter a room of beasts.")
                print("GAME OVER!")
            elif door == "yellow":
                print("\nYou found the treasure!")
                print("YOU WIN!")
            else:
                print("\nThat door doesn't exist.")
                print("GAME OVER!")

        elif action == "swim":
            print("\nYou get attacked by an angry trout.")
            print("GAME OVER!")
        else:
            print("\nInvalid choice.")
            print("GAME OVER!")

    elif direction == "right":
        print("\nYou fell into a hole.")
        print("GAME OVER!")
    else:
        print("\n Invalid direction.")
        print("GAME OVER!")


# Replay loop
while True:
    treasure_island()
    again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if again != "yes":
        print("\nThanks for playing Treasure Island!")
        break
