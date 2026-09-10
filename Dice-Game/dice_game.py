import random

print("Welcome to the game of Rolling a dice.")

while True:
    choice = input("Press 'Enter' to roll the dice or 'q' to Quit : ")
    choice = choice.strip()
    if choice == 'q':
        print("Thanks for playing the game, bye!")
        break
    elif choice == '':
        number = random.randint(1,6)
        print(f"Your Number is : {number}")
    else:
        print("Invalid input!")
print("GAME OVER !!")