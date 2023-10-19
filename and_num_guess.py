#!/usr/bin/env python3
# Created by: Anastasia Friedenstein Patino
# Created on: October. 18, 2023
# Guessing game of numbers 1 to 9
import random

# Generate a random number between 1 and 9
random_number = random.randint(1, 9)

# Get the user's guess as an integer
guess = int(input("Enter your guess:"))

# Check if the guess is correct
if guess == random_number:
    print("You guessed correctly!")
else:
    print(f"You guessed wrong. The correct answer was: {random_number}")
