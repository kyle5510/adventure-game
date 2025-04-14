# File: game.py
# Author: Kyle Auclair
# Date: April 10, 2025
# Description:
# Main script to run the text-based adventure game. Integrates town/shop/combat
# functions from gamefunctions.py and grid movement from map_screen.py.

import gamefunctions

def main():
    print("Welcome to the Adventure Game!")
    print("1) New Game\n2) Load Game")

    choice = input("Enter choice (1–2): ")
    choice = gamefunctions.validate_menu_input(choice, 1, 2)

    if choice == 1:
        name = input("Enter your name: ")
        hp = 30
        gold = 20
        inventory = []
        equipped_weapon = None
        gamefunctions.print_welcome(name)
    else:
        hp, gold, inventory, equipped_weapon = gamefunctions.load_game()

    while True:
        print("\nWhat would you like to do?")
        print("1) Leave Town")
        print("2) Visit Shop")
        print("3) Equip Item")
        print("4) Save Game")
        print("5) Quit")

        choice = input("Enter choice (1–5): ")
        choice = gamefunctions.validate_menu_input(choice, 1, 5)

        if choice == 1:
            hp, gold, inventory = gamefunctions.leave_town(hp, gold, inventory, equipped_weapon)
        elif choice == 2:
            gold, inventory = gamefunctions.visit_shop(gold, inventory)
        elif choice == 3:
            equipped_weapon = gamefunctions.equip_item(inventory)
        elif choice == 4:
            gamefunctions.save_game(hp, gold, inventory, equipped_weapon)
        elif choice == 5:
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
