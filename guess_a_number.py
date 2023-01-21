from random import randint
from colorama import Fore

upper_bored = 100

# Loop for all levels in the game
for level in range(1, 6):
    random_number = randint(1, upper_bored)
    attempts = 5

    # Loop for the current level
    while True:
        # If the attempts is more than 5, the game is over.
        if attempts <= 0:
            print(Fore.RED + "Sorry! You had 5 attempts and you don't guess a number!")
            print(f"You lose the game on {level} level.")
            exit()

        # Shows how many attempts you have and you should input your choice
        print(Fore.BLACK + f"You have {attempts} attempts to the end of a game.")
        player = input(f"Guess a number that is between 1 and {upper_bored} inclusive:")

        if not player.isdigit():
            print(Fore.RED + "Invalid input. Try again.")
            attempts -= 1
            continue

        player_number = int(player)

        # Checks if the number is correct, or if it is less than or greater than
        if player_number == random_number:
            print(Fore.GREEN + "You found a number. Congratulations!")
            print("\n")
            if level == 5:
                print("You win the GAME!")
            else:
                upper_bored += 50
            break

        elif player_number < random_number:
            attempts -= 1
            print("Try with GREATER than that.")
            continue

        elif player_number > random_number:
            attempts -= 1
            print("Try with LESS than that.")
            continue
