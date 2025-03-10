# File: gamefunctions.py
# Author: Kyle Auclair
# Date: March 9, 2025
# Description:
# This module contains functions for an adventure game. Functions include:
# print_welcome(), print_shop_menu(), purchase_item(), and random_monster().
# Additional character creation functions are included for extended gameplay.

"""
gamefunctions.py - Provides functions for an adventure game module.

This module contains functions for character creation, gameplay mechanics,
and interactions for an adventure game. Functions include welcoming the player,
displaying a shop menu, handling item purchases, and generating random monsters.

Typical usage example:

    import gamefunctions

    gamefunctions.print_welcome("Player")
    gamefunctions.print_shop_menu("Sword", 10.0, "Shield", 15.0)
    items_bought, money_left = gamefunctions.purchase_item(5.0, 20.0, 2)
    monster = gamefunctions.random_monster()
"""

import random

def print_welcome(name, width=20):
    """
    Prints a centered welcome message for the given name within a specified width.

    Args:
        name (str): The name to include in the welcome message.
        width (int): The total width of the centered message. Default is 20.

    Returns:
        None

    Example:
        >>> print_welcome("Aria")
        (centered message "Hello, Aria!")
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

    Example:
        >>> print_shop_menu("Sword", 10.0, "Shield", 15.0)
    """
    print("/--------------------\\")
    print(f"| {item1_name:<12} ${item1_price:>6.2f} |")
    print(f"| {item2_name:<12} ${item2_price:>6.2f} |")
    print("\\--------------------/")


def purchase_item(item_price, starting_money, quantity_to_purchase=1):
    """
    Calculates purchased items and remaining money after a purchase.

    Args:
        item_price (float): Price per item.
        starting_money (float): Total money available.
        quantity_to_purchase (int): Number of items to buy.

    Returns:
        tuple: Number of items purchased and remaining money.

    Example:
        >>> purchase_item(5.0, 20.0, 2)
        (2, 10.0)
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

    Example:
        >>> monster = random_monster()
        {'name': 'Goblin', 'description': 'A sneaky goblin with a rusty dagger.', 'health': 50}
    """
    monsters = [
        {"name": "Goblin", "description": "A sneaky goblin with a rusty dagger.", "health": 50},
        {"name": "Vulture", "description": "A scavenging vulture circling above.", "health": 40},
        {"name": "Troll", "description": "A towering troll with a massive club.", "health": 150}
    ]
    return random.choice(monsters)


def test_functions():
    """
    Runs test cases for all functions in this module.
    """
    print("\nTesting print_welcome()")
    print_welcome("Jeff")
    print_welcome("Audrey")
    print_welcome("Kyle")

    print("\nTesting print_shop_menu()")
    print_shop_menu("Apple", 31.00, "Pear", 1.23)
    print_shop_menu("Egg", 0.23, "Bag of Oats", 12.34)
    print_shop_menu("Bread", 2.5, "Milk", 3.99)

    print("\nTesting purchase_item()")
    print(purchase_item(5, 100, 3))
    print(purchase_item(10, 50, 10))
    print(purchase_item(7, 25, 5))

    print("\nTesting random_monster()")
    print(random_monster())
    print(random_monster())
    print(random_monster())


if __name__ == "__main__":
    test_functions()
