from random import randint
from colorama import Fore

random_number = randint(1, 100)
attempts = 5

while True:
    if attempts <= 0:
        print(Fore.RED + "Sorry! You had 5 attempts and you don't guess a number!")
        break

    print(Fore.BLACK + f"You have {attempts} attempts to the end of a game.")
    player = input("Guess a number that is between 1 and 100 inclusive:")

    if not player.isdigit():
        print(Fore.RED + "Invalid input. Try again.")
        attempts -= 1
        continue

    player_number = int(player)

    if player_number == random_number:
        print(Fore.GREEN + "You found a number. Congratulations!")
        break
    elif player_number < random_number:
        attempts -= 1
        print("Less than a number you should found.")
        continue
    elif player_number > random_number:
        attempts -= 1
        print("Large than a number you should found.")
        continue
