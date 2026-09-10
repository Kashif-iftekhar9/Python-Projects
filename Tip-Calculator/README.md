# Tip Calculator

A simple Python program that calculates how much each person should pay when splitting a bill.

## How It Works

The program asks the user for:

1. The total bill amount
2. The tip percentage
3. The number of people sharing the bill

It then calculates the total amount including the tip and divides it equally among all the people.

## Example

```text
Welcome to the Tip Calculator !

What is the total bill amount ?
100

How much tip you would like to give ?
10

How many people to split the bill ?
People : 2

Each person should pay: $55.00
````

## Formula

```text
Tip Amount = Bill × (Tip Percentage / 100)

Total Amount = Bill + Tip Amount

Amount Per Person = Total Amount / Number of People
```

## Technologies Used

* Python

## How to Run

1. Make sure Python is installed on your computer.
2. Clone this repository.
3. Open the project folder in VS Code.
4. Run the program:

```bash
python tipcalculator.py
```

## Project Structure

```text
tip-calculator/
│
├── tipcalculator.py
└── README.md
```

## Future Improvements

* Add input validation
* Allow decimal tip percentages
* Add currency selection
* Create a graphical user interface
* Improve the user experience

## Author

Kashif Iftekahr