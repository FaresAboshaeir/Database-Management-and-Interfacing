#!/usr/bin/env python3

# Author: Fares abos0008
# Date: September 27, 2025
# Version: 1.0
# Completion time: 30 minutes
# exponentiate.py
# Purpose: Square and cube integers using functions

def get_integer(prompt="Enter a number: "):
    return int(input(prompt))

def square(num):
    return num ** 2

def cube(num):
    return num ** 3

# Main program
print("This program squares and cubes an integer.")
proceed = input("Do you want to proceed? (y/n): ")

while proceed.lower() == "y":
    number = get_integer("Enter a number (0 or 1 for special case, q to quit): ")
    
    if number == 0:
        print("0")
    elif number == 1:
        print("1")
    else:
        print("Square:", square(number), "Cube:", cube(number))

    proceed = input("Do you want to continue? (y/n): ")

print("Closing program.")
