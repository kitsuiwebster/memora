# @name: Memora
# @author: kitsuiwebster

from config import streak_of_10, streak_of_50, streak_of_100, streak_of_150, streak_of_200, ascii_100, ascii_1000, ascii_goodbye, ascii_memora

import random
import json
from colorama import init, Fore

init() 

# This is the Welcome message
print(Fore.YELLOW + """
              
              Welcome to""")
print(f"{ascii_memora}" + Fore.RESET)

# This is the Goodbye message
def print_goodbye_message():
    print(f"{ascii_goodbye}")
    print(Fore.YELLOW + "And see you soon :D")

# This is the menu
def choose_game_mode():
    print(Fore.YELLOW + "******MENU*****MENU*****MENU*****MENU*****MENU*****MENU******" + Fore.RESET)
    user_choice = input("Please choose between 1 (Train your Centium), 2 (Train your Millenium) or 3 (Quit):")

    try:
        if user_choice == '1':
            with open("centium.json", "r") as file:
                data = json.load(file)
            word_map = data
            print(Fore.YELLOW + "\nYou chose Centium:\n")
            print(f"{ascii_100}")
            print("Let's start!" + Fore.RESET)

        elif user_choice == '2':
            with open("millenium.json", "r") as file:
                data = json.load(file)
            word_map = data
            print(Fore.YELLOW + "\nYou chose Millenium:\n")
            print(f"{ascii_1000}")
            print("Let's start!" + Fore.RESET)

        elif user_choice == '3':
            print_goodbye_message()
            exit(0)
        else:
            print(Fore.RED + "Invalid choice!" + Fore.RESET)
            return choose_game_mode()

    except FileNotFoundError:
        print(Fore.RED + "Oops! The required .json file is missing. Please add the file and try again." + Fore.RESET)
        return choose_game_mode() 

    return word_map

# Variables
word_map = choose_game_mode()
score = 0
best_score = 0
streak = 0
current_score = 0 

# This is the game loop
while True:
    num = random.choice(list(word_map.keys()))
    print(f"The number is: {num}")
    
    user_word = input("Enter the corresponding word: ").lower()
    
    if user_word == word_map[num]:
        score += 1 
        current_score += 1 
        streak += 1 
        print(Fore.GREEN + "Correct! Next word." + Fore.RESET)
        if streak == 10:
            for _ in range(10):
                print(Fore.GREEN + f"{streak_of_10}" + Fore.RESET)
        elif streak == 50:
            for _ in range(10):
                print(Fore.GREEN + f"{streak_of_50}" + Fore.RESET)
        elif streak == 100:
                print(Fore.GREEN + f"{streak_of_100}" + Fore.RESET)
        elif streak == 150:
            for _ in range(10):
                print(Fore.GREEN + f"{streak_of_150}" + Fore.RESET)
        elif streak == 200:
            for _ in range(1000):
                print(Fore.GREEN + f"{streak_of_200}" + Fore.RESET)
    else:
        print(Fore.RED + f"Failed! The correct answer was {word_map[num]}. Game over!" + Fore.RESET)
        print(Fore.YELLOW + f"Your score for this session is: {current_score}" + Fore.RESET)

        if current_score > best_score:  
            best_score = current_score

        streak = 0
        current_score = 0  
        print(Fore.YELLOW + f"Your best score in this session is: {best_score}" + Fore.RESET)
        print("Please choose between 1 (Continue playing), 2 (Back to Menu) or 3 (Quit):")
        retry = input().lower()
        if retry == "1":
            print(Fore.YELLOW + "The game continues!" + Fore.RESET)
        elif retry == "3":
            print_goodbye_message()
            break
        elif retry == '2':
            word_map = choose_game_mode()
            score = 0  
            streak = 0 
            best_score = 0  
        else:
            while retry not in ['1', '2', '3']:
                print(Fore.RED + "Invalid choice!" + Fore.RESET)
                print("Please choose between 1 (Continue playing), 2 (Back to Menu) or 3 (Quit):")
                retry = input().lower()
                if retry == "1":
                    print(Fore.YELLOW + "The game continues!" + Fore.RESET)
                elif retry == "3":
                    print_goodbye_message()
                    break
                elif retry == '2':
                    word_map = choose_game_mode()
                    score = 0  
                    streak = 0 
                    best_score = 0
