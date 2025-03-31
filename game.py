# File: game.py
# Author: Kyle Auclair
# Date: March 23, 2025
# Description: Main program for the adventure game. Imports gamefunctions.py and calls the required functions with user interaction.

import gamefunctions

def main():
    """Main function that runs the adventure game."""
    hp = 30
    gold = 10
    running = True

    player_name = input("What is your name, adventurer? ")
    gamefunctions.print_welcome(player_name)

    while running:
        print(f"\nYou are in town.")
        print(f"Current HP: {hp}, Current Gold: {gold}")
        print("What would you like to do?")
        print("1) Leave town (Fight Monster)")
        print("2) Sleep (Restore HP for 5 Gold)")
        print("3) Quit")
        
        choice = input("Enter choice (1-3): ")
        choice = gamefunctions.validate_menu_input(choice, 1, 3)

        if choice == 1:
            hp, gold = gamefunctions.leave_town(hp, gold)
        elif choice == 2:
            if gold >= 5:
                hp = 30
                gold -= 5
                print("You sleep and restore your HP to full.")
            else:
                print("You don't have enough gold to sleep!")
        else:
            running = False
            print("Thanks for playing! Goodbye.")

if __name__ == "__main__":
    main()
