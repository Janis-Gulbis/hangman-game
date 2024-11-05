# %%
import random

# Initialize word list and randomly select a word
word_list = ["apple", "banana", "orange", "strawberry", "melon"]
word = random.choice(word_list)

# Get user input and validate
guess = input("Please enter a single letter:")
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input")
# %%
