# %%
import random

# Initialize the word list and choose a random word
word_list = ["apple", "banana", "orange", "strawberry", "melon"]
word = random.choice(word_list)

# Define the check_guess function
def check_guess(guess):
    # Convert the guess to lowercase
    guess = guess.lower()
    
    # Check if the guess is in the word
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

# Define the ask_for_input function
def ask_for_input():
    while True:
        # Prompt the user to enter a letter and validate the input
        guess = input("Please enter a single letter: ").strip().lower()
        
        # Check if the guess is a single alphabetical character
        if len(guess) == 1 and guess.isalpha():
            # Call check_guess if the input is valid
            check_guess(guess)
            break  # Exit the loop once a valid guess has been processed
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

# Calls ask_for_input to test the code
ask_for_input()
# %%
