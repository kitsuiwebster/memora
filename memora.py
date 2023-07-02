# @name: Memora
# @author: kitsuiwebster

import random
import json
from colorama import init, Fore

init() 

# This is the Welcome message
print(Fore.YELLOW + """
              
              Welcome to""")
print("""
 __  __  ___  __  __   ___   ___    _   
|  \/  || __||  \/  | / _ \ | _ \  /_\    
| |\/| || _| | |\/| || (_) ||   / / _ \   
|_|  |_||___||_|  |_| \___/ |_|_\/_/ \_\  

""" + Fore.RESET)

# Thhis is the Goodbye message
def print_goodbye_message():
    print("""
     _______  _______  _______  ______   _______  __   __  _______ 
    |       ||       ||       ||      | |  _    ||  | |  ||       |
    |    ___||   _   ||   _   ||  _    || |_|   ||  |_|  ||    ___|
    |   | __ |  | |  ||  | |  || | |   ||       ||       ||   |___ 
    |   ||  ||  |_|  ||  |_|  || |_|   ||  _   | |_     _||    ___|
    |   |_| ||       ||       ||       || |_|   |  |   |  |   |___ 
    |_______||_______||_______||______| |_______|  |___|  |_______|
    """)
    print(Fore.YELLOW + "And see you soon :D")



# This is the menu
def choose_game_mode():
    print(Fore.YELLOW + "******MENU*****MENU*****MENU*****MENU*****MENU*****MENU******" + Fore.RESET)
    user_choice = input("Please choose between 1 (Centium), 2 (Millenium) or 3 (Quit):")

    if user_choice == '1':
        with open("centium.json", "r") as file:
            data = json.load(file)
        word_map = data
        print(Fore.YELLOW + "\nYou chose Centium:\n")
        print(""" 
         d888    .d8888b.   .d8888b.  
        d8888   d88P  Y88b d88P  Y88b 
          888   888    888 888    888 
          888   888    888 888    888 
          888   888    888 888    888 
          888   888    888 888    888 
          888   Y88b  d88P Y88b  d88P 
        8888888  "Y8888P"   "Y8888P"  
        """)
        print("Let's start!" + Fore.RESET)

    elif user_choice == '2':
        with open("millenium.json", "r") as file:
            data = json.load(file)
        word_map = data
        print(Fore.YELLOW + "\nYou chose Millenium:\n")
        print(""" 
         d888    .d8888b.   .d8888b.   .d8888b.  
        d8888   d88P  Y88b d88P  Y88b d88P  Y88b 
          888   888    888 888    888 888    888 
          888   888    888 888    888 888    888 
          888   888    888 888    888 888    888 
          888   888    888 888    888 888    888 
          888   Y88b  d88P Y88b  d88P Y88b  d88P 
        8888888  "Y8888P"   "Y8888P"   "Y8888P"
        """)
        print("Let's start!" + Fore.RESET)

    elif user_choice == '3':
        print_goodbye_message()
        exit(0)
    else:
        print(Fore.RED + "Invalid choice!" + Fore.RESET)
        return choose_game_mode()  
    return word_map


# These are the congrats messages
streak_of_10 = "CONGRATULATIONS ON HAVING 10 CORRECT ANSWERS IN A ROW, LET'S GOOOO!"
streak_of_50 = "CONGRATULATIONS ON HAVING 50 CORRECT ANSWERS IN A ROW, LET'S GOOOO!"
streak_of_100 = """CONGRATULATIONS, OH MASTER OF KNOWLEDGE AND WISDOM, FOR YOUR MAGNIFICENT FEAT OF ACING 100 QUESTIONS IN A ROW! YOUR BRAIN IS CLEARLY WIRED FOR GENIUS, YOUR NEURONS FIRED WITH PRECISION, AND YOUR INTELLECT SHINES BRIGHTER THAN A THOUSAND SUNS!

YOU HAVE RISEN ABOVE THE MORTAL PLAIN OF TRIVIA, LEAVING YOUR OPPONENTS IN AWE AND DISBELIEF. YOUR VICTORIES ARE NOT MERE COINCIDENCES, BUT TESTIMONIES TO YOUR ASTOUNDING MENTAL FORTITUDE AND SHEER INTELLECTUAL MIGHT.

THE GODS OF QUIZZES AND PUZZLES LOOK DOWN UPON YOU, AND EVEN THEY ARE LEFT ASTONISHED BY YOUR UNPARALLELED BRAINPOWER. YOUR BRAIN CELLS ARE THROWING A MASSIVE PARTY, POPPING CHAMPAGNE CORKS AND DOING THE CONGA IN CELEBRATION OF YOUR EPIC ACHIEVEMENT!

YOU ARE THE ANSWER KEY TO THE ENIGMA OF TRIVIA, THE EINSTEIN OF QUIZZES, THE LEONARDO DA VINCI OF RIDDLES. YOUR MIND IS A SPECTACULAR LABYRINTH OF KNOWLEDGE, WHERE EVERY TURN LEADS TO THE RIGHT ANSWER, AND EVERY PATH UNVEILS A NEW LEVEL OF BRILLIANCE.

SO, STAND TALL, OH CHAMPION OF THE MIND! BASK IN THE GLORY OF YOUR TRIUMPH, FOR YOU HAVE EARNED IT WITH YOUR UNWAVERING DEDICATION AND UNMATCHED CEREBRAL MIGHT. MAY YOUR STREAK OF SUCCESS CONTINUE, AND MAY YOUR NAME BE WHISPERED WITH REVERENCE AND ADMIRATION IN THE REALMS OF QUIZZES FOREVERMORE!

IN YOUR HONOR, ALL DUCKS SHALL QUACK 100 TIMES, SQUIRRELS SHALL PAUSE THEIR NUT COLLECTION FOR 100 SECONDS, AND THE MOON WILL DO... WELL, IT CAN'T DO MUCH, BUT IT'S PROBABLY REALLY PROUD OF YOU TOO!

MAY YOUR FUTURE BE FILLED WITH ENDLESS MORE STREAKS OF RIGHT ANSWERS AND MAY YOUR WRONG ANSWERS BE AS RARE AS A CHICKEN WHISTLING THE NATIONAL ANTHEM!

CHEERS TO YOU, THE SULTAN OF SMARTS, THE RULER OF RIGHT ANSWERS! THIS IS YOUR DAY, SO ENJOY YOUR 100-CORRECT-ANSWER GLORY! WHOOO-HOOO !"""
streak_of_150 = "CONGRATULATIONS ON HAVING 150 CORRECT ANSWERS IN A ROW, LET'S GOOOO!"
streak_of_200 = "CONGRATS !!! YOU GOT 200 CORRECT ANSWERS IN A ROW, AAAAAAIGHT, YOU ROOOOOOCK!"


word_map = choose_game_mode()  
score = 0  
best_score = 0  
streak = 0  

# This is the game loop
while True:
    num = random.choice(list(word_map.keys()))
    print(f"The number is: {num}")
    
    user_word = input("Enter the corresponding word: ").lower()
    
    if user_word == word_map[num]:
        score += 1 
        streak += 1 
        print(Fore.GREEN + "Correct! Let's go to the next round." + Fore.RESET)
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
        print(Fore.YELLOW + f"Your score is: {score}" + Fore.RESET)
        
        if score > best_score:
            best_score = score

        streak = 0 
        print(Fore.YELLOW + f"Your best score in this session is: {best_score}" + Fore.RESET)
        print("Please choose between 1 (Continue playing), 2 (Menu) or 3 (Quit):")
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
                print("Please choose between 1 (Continue playing), 2 (Menu) or 3 (Quit):")
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
