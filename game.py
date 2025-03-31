# File: game.py
# Author: Kyle Auclair
# Date: March 30, 2025
# Description:
# Main program for the adventure game. Imports gamefunctions.py and calls the
# required functions with user interaction, including inventory and item usage.

import gamefunctions

def main():
    """Main function that runs the adventure game."""
    hp = 30
    gold = 20
    inventory = []
    equipped_weapon = None
    running = True

    player_name = input("What is your name, adventurer? ")
    gamefunctions.print_welcome(player_name)

    while running:
        print("\nYou are in town.")
        print(f"Current HP: {hp}, Current Gold: {gold}")
        print("What would you like to do?")
        print("1) Leave town (Fight Monster)")
        print("2) Sleep (Restore HP for 5 Gold)")
        print("3) Visit Shop")
        print("4) Equip Item")
        print("5) Quit")

        choice = input("Enter choice (1–5): ")
        choice = gamefunctions.validate_menu_input(choice, 1, 5)

        if choice == 1:
            hp, gold, inventory = gamefunctions.leave_town(hp, gold, inventory, equipped_weapon)
        elif choice == 2:
            if gold >= 5:
                hp = 30
                gold -= 5
                print("You sleep and restore your HP to full.")
            else:
                print("You don't have enough gold to sleep!")
        elif choice == 3:
            gold, inventory = gamefunctions.visit_shop(gold, inventory)
        elif choice == 4:
            equipped_weapon = gamefunctions.equip_item(inventory)
        elif choice == 5:
            running = False
            print("Thanks for playing! Goodbye.")

if __name__ == "__main__":
    main()
