# Number Guessing Game

A simple command-line number guessing game built with Python.

The computer randomly selects a secret number between 1 and 50, and the player gets 10 attempts to guess it correctly.

## Features

- Randomly generates a secret number between 1 and 50
- Gives the player 10 attempts
- Shows the number of attempts remaining
- Gives a "Higher" or "Lower" hint after an incorrect guess
- Displays a winning message when the number is guessed
- Reveals the secret number when the game ends

## How It Works

When the game starts, the computer generates a random number between 1 and 50.

The player enters a guess and receives feedback:

- If the guess is correct → You WIN!
- If the guess is too low → Try a **Higher** number
- If the guess is too high → Try a **Lower** number
- After 10 incorrect attempts → The game ends

The secret number is generated using Python's `random` module. :contentReference[oaicite:1]{index=1}

## Example

```text
Welcome to the number guessing game.
We have a number that need to be guessed.
You have 10 chances.

The secret number is between 1 to 50

You have 10 attempts left.

Guess a number : 25

Your Guess is Wrong! Try Higher number

You have 9 attempts left.

Guess a number : 37

You WON !!

The Secret Number is 37. GAME OVER !!
````

## Technologies Used

* Python
* Random Module
* While Loop
* Conditional Statements
* User Input

## How to Run

Make sure Python is installed on your computer.

Run the following command:

```bash
python guess_the_number.py
```

## Project Structure

```text
number-guessing-game/
│
├── guess_the_number.py
└── README.md
```

## Future Improvements

* Add difficulty levels
* Allow the player to choose the number range
* Add a scoring system
* Add multiple rounds
* Keep track of the best score
* Add input validation for invalid entries

## Author
Kashif Iftekhar