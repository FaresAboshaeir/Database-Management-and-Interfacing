#!/usr/bin/env python3

# display_menu.py
# Purpose: Display a menu and get user choice
# Author: Fares abos0008
# Date: September 27, 2025
# Version: 1.0
# Completion time: 15m

def show_menu():
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    return

def get_menu_choice(prompt):
    choice = input(prompt)
    return choice

# Main program
show_menu()
menu_choice = get_menu_choice("Select a menu option: ")
print("You selected:", menu_choice)
