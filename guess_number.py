#!/usr/bin/python3

"""
Program name: guess_number.py
Program purpose: Let the user guess a random number between 1 and 9
Author: Fares abos0008, 041087275, Section: 013
Date & version: 2025-09-22, version 1.0
Completion time: 30 minutes
"""

import random

# generate secret number
secret = random.randint(1, 9)

# prompt for first guess
guess = int(input("Guess a number from 1 – 9 (0 to quit): "))

# read loop
while guess != 0 and guess != secret:
    if guess < secret:
        print("Your guess is too low: guess higher.")  # hint
    elif guess > secret:
        print("Your guess is too high: guess lower.")  # hint

    # reprompt
    guess = int(input("Guess again from 1 – 9 (0 to quit): "))

# correct guess
if guess == secret:
    print("Congratulations:", secret, "is a match!")

# closing message
print("Thank you for playing Guess the Number.")
