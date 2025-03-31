# File: gamefunctions.py
# Author: Kyle Auclair
# Date: March 23, 2025
# Description: This module contains functions for an adventure game. Functions include: 
# print_welcome(), print_shop_menu(), purchase_item(), random_monster().
# Additional combat functions and input validation are included for gameplay.

import random

def print_welcome(name, width=20):
    """Prints a centered welcome message for the given name."""
    message = f"Hello, {name}!"
    print(f"{message:^{width}}")

def validate_menu_input(choice, min_val, max_val):
    """Validates menu input from user within a range."""
    while True:
        try:
            num = int(choice)
            if num < min_val or num > max_val:
                raise ValueError
            return num
        except ValueError:
            choice = input(f"Invalid input! Enter a number between {min_val} and {max_val}: ")

def random_monster():
    """Returns a randomly selected monster from a predefined list."""
    monsters = [
        {"name": "Goblin", "description": "A sneaky goblin with a rusty dagger"},
        {"name": "Vulture", "description": "A scavenging vulture circling above"},
        {"name": "Troll", "description": "A towering troll with a massive club"}
    ]
    return random.choice(monsters)

def leave_town(hp, gold):
    """Handles leaving town to fight a monster."""
    print("\nYou leave town and encounter a monster!")
    monster = random_monster()
    monster_hp = random.randint(10, 20)
    print(f"A wild {monster['name']} appears!")
    print(monster['description'])
    
    fighting = True
    while fighting:
        print(f"\nYour HP: {hp} | {monster['name']} HP: {monster_hp}")
        print("1) Attack")
        print("2) Run Away")

        choice = input("Choose an action (1-2): ")
        choice = validate_menu_input(choice, 1, 2)

        if choice == 1:
            player_damage = random.randint(4, 8)
            monster_damage = random.randint(2, 5)
            monster_hp -= player_damage
            hp -= monster_damage
            print(f"You hit the {monster['name']} for {player_damage} damage!")
            print(f"The {monster['name']} hits you for {monster_damage} damage!")

            if monster_hp <= 0:
                print(f"You defeated the {monster['name']}!")
                gold_earned = random.randint(5, 15)
                gold += gold_earned
                print(f"You found {gold_earned} gold!")
                fighting = False
        elif choice == 2:
            print("You run back to town!")
            fighting = False

        if hp <= 0:
            print("You have been defeated!")
            fighting = False

    return hp, gold
