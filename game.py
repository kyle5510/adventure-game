# File: game.py
# Author: Kyle Auclair
# Date: April 6, 2025
# Description:
# Main program for the adventure game. Handles user interaction and calls
# supporting functions from gamefunctions.py, including options to save/load
# the game, manage inventory, and battle monsters.

import gamefunctions

def main():
    hp = 30
    gold = 20
    inventory = []
    equipped_weapon = None
    running = True

    print("Welcome to the Adventure Game!")
    print("1) Start New Game")
    print("2) Load Saved Game")

    start_choice = input("Enter choice: ")
    start_choice = gamefunctions.validate_menu_input(start_choice, 1, 2)

    if start_choice == 2:
        hp, gold, inventory, equipped_weapon = gamefunctions.load_game()
    else:
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
        print("5) Save and Quit")

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
            gamefunctions.save_game(hp, gold, inventory, equipped_weapon)
            running = False
            print("Game saved and quitting. Goodbye!")

if __name__ == "__main__":
    main()
