# File: gamefunctions.py
# Author: Kyle Auclair
# Date: March 23, 2025
# Description:
# Contains all supporting functions for the adventure game, including user input
# validation, printing the welcome message, and the logic for leaving town and
# fighting a monster.

import random

def print_welcome(name):
    """Prints a welcome message to the user."""
    print(f"\nWelcome, {name}! Your adventure begins now.")

def validate_menu_input(choice, min_val, max_val):
    """Validates that the user input is a number within the given range."""
    while True:
        try:
            num = int(choice)
            if num < min_val or num > max_val:
                raise ValueError
            return num
        except ValueError:
            choice = input(f"Invalid input. Please enter a number between {min_val} and {max_val}: ")

def leave_town(hp, gold):
    """Handles the monster battle system."""
    monster_hp = 20
    print("\nYou leave town and encounter a wild monster!")

    while monster_hp > 0 and hp > 0:
        print(f"\nYour HP: {hp} | Monster HP: {monster_hp}")
        print("What will you do?")
        print("1) Attack")
        print("2) Run")
        choice = input("Enter your choice (1–2): ")
        choice = validate_menu_input(choice, 1, 2)

        if choice == 1:
            damage_to_monster = random.randint(4, 8)
            damage_to_player = random.randint(2, 6)
            monster_hp -= damage_to_monster
            hp -= damage_to_player
            print(f"\nYou hit the monster for {damage_to_monster} damage!")
            print(f"The monster hits you for {damage_to_player} damage!")
        elif choice == 2:
            print("\nYou run away and return safely to town.")
            return hp, gold

    if monster_hp <= 0:
        print("\nYou defeated the monster! You earn 10 gold.")
        gold += 10
    elif hp <= 0:
        print("\nYou were defeated and crawl back to town with 10 HP.")
        hp = 10  # Optionally restore player to low HP instead of ending game

    return hp, gold
