#!/usr/bin/env python3

# check_even.py
# Purpose: Check if a number is even or odd
# Author: Fares abos0008
# Date: September 27, 2025
# Version: 1.0
# Completion time: 10m

def iseven(num):
    return num % 2 == 0

# Main program
number = int(input("Enter an integer: "))
if iseven(number):
    print("This is an even number.")
else:
    print("This is an odd number.")
