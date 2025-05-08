
from gamefunctions import *
from map_screen import launch_map
from wanderingMonster import initialize_monsters

def main():
    print_welcome()
    load_game()
    monsters = initialize_monsters()
    while True:
        print("\n--- Main Menu ---")
        print("1. Enter Map")
        print("2. Shop")
        print("3. Equip Item")
        print("4. Use Item")
        print("5. Sleep")
        print("6. Save Game")
        print("7. Quit")

        choice = input("Choose an action: ")
        if choice == "1":
            launch_map(monsters)
        elif choice == "2":
            print_shop_menu()
            item = input("Enter item name to purchase: ").lower()
            purchase_item(item)
        elif choice == "3":
            item = input("Enter item to equip: ").lower()
            equip_item(item)
        elif choice == "4":
            item = input("Enter item to use: ").lower()
            use_item(item)
        elif choice == "5":
            sleep()
        elif choice == "6":
            save_game()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
