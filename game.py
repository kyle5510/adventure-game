# File: game.py
# Author: Kyle Auclair
# Date: March 9, 2025
# Description:
# Main program for the adventure game. Imports gamefunctions and calls the
# required functions with user interaction.

import gamefunctions

def main():
    """
    Main function that runs the adventure game.
    """
    # Welcome message with user input
    player_name = input("What is your name, adventurer? ")
    gamefunctions.print_welcome(player_name)

    # Show shop menu and get item choices
    print("\nWelcome to the shop!")
    item1_name = "Sword"
    item1_price = 10.0
    item2_name = "Shield"
    item2_price = 15.0

    gamefunctions.print_shop_menu(item1_name, item1_price, item2_name, item2_price)

    # Prompt player to purchase an item
    chosen_item = input(f"\nWhich item would you like to buy? ({item1_name}/{item2_name}): ")

    # For simplicity, use a fixed price and balance
    starting_money = 50.0
    if chosen_item.lower() == item1_name.lower():
        quantity = int(input(f"How many {item1_name}s would you like to buy? "))
        items_bought, money_left = gamefunctions.purchase_item(item1_price, starting_money, quantity)
        print(f"\nYou bought {items_bought} {item1_name}(s). You have ${money_left:.2f} left.")
    elif chosen_item.lower() == item2_name.lower():
        quantity = int(input(f"How many {item2_name}s would you like to buy? "))
        items_bought, money_left = gamefunctions.purchase_item(item2_price, starting_money, quantity)
        print(f"\nYou bought {items_bought} {item2_name}(s). You have ${money_left:.2f} left.")
    else:
        print("\nYou didn't buy anything!")

    # Encounter a random monster
    print("\nYou venture into the dark forest...")
    monster = gamefunctions.random_monster()
    print(f"A wild {monster['name']} appears!")
    print(monster["description"])
    print(f"It has {monster['health']} health points!")

if __name__ == "__main__":
    main()
