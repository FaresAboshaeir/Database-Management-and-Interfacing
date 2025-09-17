#!/usr/bin/python3

"""
Program name: guess_course.py
Program purpose: Repeatedly prompt for course number until correct or quit
Author: Fares abos0008, 041087275, Section: 013
Date & version: 2025-09-17 v1.0
"""

# Constant course code (convention: ALL CAPS)
COURSE_CODE = "CST8245"

# Initial prompt with quit option
guess = input('Enter the course number (q to quit): ')

# While guess is incorrect AND user doesn't want to quit
while guess != COURSE_CODE and guess != "q":
    guess = input('Not correct. Try again (q to quit): ')

# Closing message
print("Thank you.")
