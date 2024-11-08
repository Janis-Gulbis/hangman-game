# hangman-game 🎮
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

Welcome to the Hangman Game project! This is a Python-based implementation of the classic word-guessing game where players try to guess the hidden word by suggesting letters within a limited number of attempts.

## Table of Content
* Project Description
* Features
* Learning Objectives
* Installation
* Usage
* Licence

## Project Description
This project is a command-line game built in Python that simulates the game of Hangman. A word is chosen randomly from a list of words, and the player must guess the word letter by letter. Each incorrect guess costs the player a life. The game ends when either:

* The player successfully guesses the word, or
* The player runs out of lives.

This project also showcases good practices in Python programming, including:

* Classes and object-oriented programming.
* Methods to validate user input.
* Looping constructs and conditionals.
* Basic data manipulation with lists and strings.

## Features
* Random Word Selection: A random word is chosen from a predefined list at the start of each game.
* Input Validation: Ensures that each guess is a single, alphabetical character that hasn't already been guessed.
* Life Counter: Tracks remaining lives and ends the game when lives reach zero.
* Dynamic Word Reveal: Shows the player’s progress by revealing correct guesses in the hidden word.
* Win and Lose Scenarios: Congratulates the player on a win, or displays a loss message if lives run out.

## Learning Objectives
This project aims to reinforce fundamental programming concepts:

* Working with classes and instance attributes in Python.
* Using loops, conditionals, and functions effectively.
* Implementing data validation for user input.
* Using lists, strings, and basic data manipulation techniques.
* Creating a simple command-line game experience.

## Installation
To get started with the Hangman Game, follow these steps:

1. Clone the Repository: ` https://github.com/Janis-Gulbis/hangman-game.git `

   `cd hangman-game`

1. Ensure Python is Installed: This project requires Python 3.x. You can download Python from [python.org](https://www.python.org/)
1. Run the game: Execute the game by running the script directly.

   `python milestone_5.py`

## Usage
To play the game:

1. Start the script and follow the on-screen prompts to guess letters.
2. Input a single alphabetical letter as your guess.
3. Keep guessing until you either guess the word correctly or run out of lives.

## Key files

* `milestone_5.py` : Contains the main logic and methods for the Hangman game, including:
* `Hangman` class for managing game atributes and mechanics.
* `play_game` function to initialize and run the game loop.

## License
This project is licensed under the `MIT` License.


