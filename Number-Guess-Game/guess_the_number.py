"""
A simple number guessing game.
The user gets 10 chances to guess a number.
If the user guesses the number before 10 chances, stop asking the number from the user
say Congrats and end the game 
if the user never guesses the number, ask them 10 times and end the game!!
"""

import random

print("Welcome to the number guessing game. We have a number that need to be guessed. you have 10 chances.")
print("The seceret number is between 1 to 50")

attempts = 10
count = 1
is_guess_correct = False
guess = random.randint(1,50)
while count <= 10:
    print(f"You have {attempts} attempts left.")
    user = int(input("\nGuess a number : "))
    if user == guess:
        print("\nYou WON !!\n")
        is_guess_correct = True
        break
    else:
        if user < guess:
            h_or_l = "Higher"
        else:
            h_or_l = "Lower"    
        print(f"\nYou Guess is Wrong ! Try {h_or_l} number\n")
    count += 1
    attempts -= 1
if is_guess_correct == False:
    print("\nBAD LUCK !! You exausted all your attempts couldn't guess the number.\n")
print(f"The Secrete Number is {guess}. GAME OVER !!")