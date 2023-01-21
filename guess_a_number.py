from random import randint
from colorama import Fore

random_number = randint(1, 100)

while True:
    player = input(Fore.BLACK + "Guess a number that is between 1 and 100 inclusive:")

    if not player.isdigit():
        print(Fore.RED + "Invalid input. Try again.")
        continue

    player_number = int(player)

    if player_number == random_number:
        print(Fore.GREEN + "You found a number. Congratulations!")
        break
    elif player_number < random_number:
        print(Fore.RED + "Less than a number you should found.")
        continue
    elif player_number > random_number:
        print(Fore.RED + "Large than a number you should found.")
        continue
