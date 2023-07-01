# @name: Cawdrey
# @author: kitsuiwebster

import random
import json
from colorama import init, Fore

init()  # initialize the colorama

# Load the JSON data
with open("centium.json", "r") as file:
    data = json.load(file)

# Insert the JSON data into word_map
word_map = data


score = 0  # Initialize the score
best_score = 0  # Initialize the best score
streak = 0  # Initialize the streak count

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

print(""" 
                                                                                                                                                 
 d888    .d8888b.   .d8888b.  
d8888   d88P  Y88b d88P  Y88b 
  888   888    888 888    888 
  888   888    888 888    888 
  888   888    888 888    888 
  888   888    888 888    888 
  888   Y88b  d88P Y88b  d88P 
8888888  "Y8888P"   "Y8888P"  

Welcome to the Centium Learner !                                                                   
""")
# Game loop
while True:
    # Choose a random number.
    num = random.choice(list(word_map.keys()))
    print(f"The number is: {num}")
    
    # Ask the user to enter the corresponding word.
    user_word = input("Enter the corresponding word: ").lower()
    
    # Check if the word is correct.
    if user_word == word_map[num]:
        score += 1  # Increase the score
        streak += 1  # Increase the streak
        print(Fore.GREEN + "Correct! Let's go to the next round." + Fore.RESET)
        # Print messages when user hits specific streak milestones
        if streak == 10:
            for _ in range(10):
                print(Fore.GREEN + f"{streak_of_10}" + Fore.RESET)
        elif streak == 50:
            for _ in range(10):
                print(Fore.GREEN + f"{streak_of_50}" + Fore.RESET)
        elif streak == 100:
            for _ in range(10):
                print(Fore.GREEN + f"{streak_of_100}" + Fore.RESET)
        elif streak == 200:
            for _ in range(1000):
                print(Fore.GREEN + f"{streak_of_200}" + Fore.RESET)
    else:
        print(Fore.RED + f"Failed! the correct answer was {word_map[num]}. Game over!" + Fore.RESET)
        print(Fore.YELLOW + f"Your score is: {score}" + Fore.RESET)
        
        # Update the best score if the current score is higher.
        if score > best_score:
            best_score = score

        streak = 0  # Reset the streak
        
        print("Press 'Enter' to retry or 'q' to quit.")
        retry = input().lower()
        if retry == "q":
            print(Fore.YELLOW + f"Your best score in this session is: {best_score}" + Fore.RESET)
            print("""
 _______  _______  _______  ______   _______  __   __  _______ 
|       ||       ||       ||      | |  _    ||  | |  ||       |
|    ___||   _   ||   _   ||  _    || |_|   ||  |_|  ||    ___|
|   | __ |  | |  ||  | |  || | |   ||       ||       ||   |___ 
|   ||  ||  |_|  ||  |_|  || |_|   ||  _   | |_     _||    ___|
|   |_| ||       ||       ||       || |_|   |  |   |  |   |___ 
|_______||_______||_______||______| |_______|  |___|  |_______|
And cy@ soon :D 
            """)
            break
        else:
            score = 0  # Reset the score

