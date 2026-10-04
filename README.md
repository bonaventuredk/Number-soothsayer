# Number Guessing Game

This project is a simple number guessing game written in Python.
The player tries to guess a secret number between a minimum and maximum value within a limited number of attempts.

## Author

### DOHEMETO Bonaventure


## Features

- Player name support
- Random secret number generation
- Attempts counter
- Hint messages such as "too low" or "too high"
- Winning and losing conditions
- Simple console-based interface

## Project files

- `Joueur.py`: defines the player class
- `JeuDevinette.py`: contains the main game logic
- `main.py`: starts the game
- `test.py`: includes unit tests for the game

## How to run

From the project folder, run:

```bash
python3 main.py
```

## Example gameplay

```text
Welcome to the Number Guessing Game!
Enter your name: Alice
Welcome Alice!
I picked a number between 0 and 10. You have 5 attempts.

Attempts left: 5
Please Alice, enter your guess: 5
Too low! Try a higher number.
```

## Testing

```bash
python3 -m unittest test.py
```
