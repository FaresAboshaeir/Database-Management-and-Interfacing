#!/usr/bin/python3

"""
Program name: parity_ctr.py
Program purpose: Count how many odd and even numbers the user enters
Author: Fares abos0008, 041087275, Section: 013
Date & version: 2025-09-22, version 1.0
Completion time: 30 minutes
"""

# initialize counters
odd_ctr = 0
even_ctr = 0

# prompt for first number
number = int(input("Enter an integer (0 to quit): "))

# read loop
while number != 0:
    # check if number is odd or even
    if number % 2 == 0:
        even_ctr += 1  # increment even counter
    else:
        odd_ctr += 1   # increment odd counter

    # reprompt for next number
    number = int(input("Enter an integer (0 to quit): "))

# display results
print("You entered", odd_ctr, "odd numbers and", even_ctr, "even numbers.")

# closing message
print("Thank you for using the odd-even counter.")
