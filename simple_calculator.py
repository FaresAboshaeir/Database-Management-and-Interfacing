#!/usr/bin/python3

"""
Program name: simple_calculator.py
Program purpose: Perform simple calculations with +, -, *, /
Author: Fares abos0008, 041087275, Section:013
Date & version: 2025-09-22, version 1.0
Completion time: ~15 minutes
"""

# prompt for operator
operator = input("Enter operator [+, -, *, /] (q to quit): ")

# loop until user quits
while operator.upper() != "Q":
    # prompt for operands
    number_1 = float(input("Enter first number: "))
    number_2 = float(input("Enter second number: "))

    # calculate based on operator
    if operator == "+":
        result = number_1 + number_2
    elif operator == "-":
        result = number_1 - number_2
    elif operator == "*":
        result = number_1 * number_2
    elif operator == "/":
        # validate divisor
        while number_2 == 0:
            number_2 = float(input("Divisor cannot be zero. Enter a valid divisor: "))
        result = number_1 / number_2
    else:
        result = "Invalid operator"

    # display result
    print("-> Result of:", number_1, operator, number_2, "=", result)

    # reprompt for operator
    operator = input("Enter operator [+, -, *, /] (q to quit): ")

# closing message
print("Closing calculator")
