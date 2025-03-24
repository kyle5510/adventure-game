# File: gamefunctions.py
# Author: Kyle Auclair
# Date: March 23, 2025
# Description:
# This module contains functions for an adventure game. Functions include:
# print_welcome(), print_shop_menu(), purchase_item(), and random_monster().
# Additional combat functions and input validation are included for gameplay.

import random

def print_welcome(name, width=20):
    """
    Prints a centered welcome message for the given name within a specified width.

    Args:
        name (str): The name to include in the welcome message.
        width (int): The total width of the centered message. Default is 20.

    Returns:
        None
    """
    message = f"Hello, {name}!"
    print(f"{message:^{width}}")

def print_shop_menu(item1_name, item1_price, item2_name, item2_price):
    """
    Prints a formatted shop menu for two items with their prices.

    Args:
        item1_name (str): Name of the first item.
        item1_price (float): Price of the first item.
        item2_name (str): Name of the second item.
        item2_price (float): Price of the second item.

    Returns:
        None
    """
    print("/----------------------\\")
    print(f"| {item1_name:<12} ${item1_price:>6.2f} |")
    print(f"| {item2_name:<12} ${item2_price:>6.2f} |")
    print("\\----------------------/")

def purchase_item(item_price, starting_money, quantity_to_purchase=1):
    """
    Calculates purchased items and remaining money after a purchase.

    Args:
        item_price (float): Price per item.
        starting_money (float): Total money available.
        quantity_to_purchase (int): Number of items to buy.

    Returns:
        tuple: Number of items purchased and remaining money.
    """
    total_cost = item_price * quantity_to_purchase
    if total_cost <= starting_money:
        return quantity_to_purchase, round(starting_money - total_cost, 2)
    else:
        affordable_quantity = int(starting_money // item_price)
        remaining_money = round(starting_money - (affordable_quantity * item_price), 2)
        return affordable_quantity, remaining_money

def random_monster():
    """
    Returns a randomly selected monster from a predefined list.

    Returns:
        dict: Randomly selected monster details.
    """
    monsters = [
        {"name": "Goblin", "description": "A sneaky goblin with a rusty dagger"},
        {"name": "Vulture", "description": "A scavenging vulture circling above"},
        {"name": "Troll", "description": "A towering troll with a massive club"}
    ]
    return random.choice(monsters)

def validate_menu_input(choice, min_val, max_val):
    """
    Validates menu input from user within a range.

    Args:
        choice (str): Initial user input.
        min_val (int): Minimum valid option.
        max_val (int): Maximum valid option.

    Returns:
        int: Validated menu choice.
    """
    while True:
        try:
            num = int(choice)
            if num < min_val or num > max_val:
                raise ValueError
            return num
        except ValueError:
            choice = input(f"Invalid input! Enter a number between {min_val} and {max_val}: ")

def leave_town(hp, gold):
    """
    Handles leaving town to fight a monster.

    Args:
        hp (int): Player's current HP.
        gold (int): Player's current gold.

    Returns:
        tuple: Updated HP and gold after the encounter.
    """
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

            if hp <= 0:
                print("You have been defeated!")
                fighting = False
        elif choice == 2:
            print("You run back to town!")
            fighting = False

    return hp, gold
