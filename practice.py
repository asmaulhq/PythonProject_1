#print("Hello World")

#name = input("WHat is you name: ")
#print("Hello " + name)
"""
your_favorite_language = input("What's your favorite programming language?: ")

if your_favorite_language=="Python":
    print("Great! Python would help you understand the future AI development.")
else:
    print("You love "+your_favorite_language +" programming language.")
"""

# Gues number
import random
random_number = random.randint(1, 10)
guess = 0
while guess != random_number:
    guess_text = input("Guess a number between 1 and 10: ")
    guess = int(guess_text)