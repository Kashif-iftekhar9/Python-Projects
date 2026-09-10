# Dice Game

A simple command-line dice game built with Python.

The program allows the user to roll a virtual dice by pressing Enter. Each roll generates a random number between 1 and 6.

## Features

- Roll the dice by pressing Enter
- Generate a random number from 1 to 6
- Quit the game by pressing `q`
- Handle invalid input

## How It Works

When the game starts, the user is asked:

```text
Press 'Enter' to roll the dice or 'q' to Quit :
````

* Press **Enter** → Roll the dice
* Press **q** → Quit the game
* Any other input → Shows an invalid input message

The game uses Python's `random` module to generate the dice number. 

## Example

```text
Welcome to the game of Rolling a dice.

Press 'Enter' to roll the dice or 'q' to Quit :
Your Number is : 4

Press 'Enter' to roll the dice or 'q' to Quit :
Your Number is : 2

Press 'Enter' to roll the dice or 'q' to Quit :
q

Thanks for playing the game, bye!
GAME OVER !!
```

## Technologies Used

* Python
* Random Module
* Loops
* Conditional Statements
* User Input

## How to Run

Make sure Python is installed on your computer.

Run the following command:

```bash
python dice_game.py
```

## Project Structure

```text
dice-game/
│
├── dice_game.py
└── README.md
```

## Future Improvements

* Add a score system
* Allow the user to choose the number of dice
* Add a two-player mode
* Keep track of total rolls
* Add a graphical interface

## Author

Kashif Iftekhar