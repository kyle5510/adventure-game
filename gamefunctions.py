
"""Game helper functions"""
import json
from random import choice

SAVE_FILE = "save_data.json"

def print_welcome():
    print("\nYou are in town.")
    print("Current HP: 30, Current Gold: 20")

def print_shop_menu():
    print("Welcome to the shop!")
    print("1) Buy Sword (10 gold)")
    print("2) Buy Rock (1 gold)")
    print("3) Leave shop")

def purchase_item(player_data):
    while True:
        print_shop_menu()
        choice = input("Choose an item to buy: ")
        if choice == "1" and player_data["gold"] >= 10:
            player_data["inventory"].append("sword")
            player_data["gold"] -= 10
            print("You bought a sword!")
        elif choice == "2" and player_data["gold"] >= 1:
            player_data["inventory"].append("rock")
            player_data["gold"] -= 1
            print("You bought a rock!")
        elif choice == "3":
            break
        else:
            print("Invalid choice or not enough gold.")
    return player_data

def equip_item(player_data):
    print("Choose a weapon to equip:")
    weapons = list(set(player_data["inventory"]))
    for idx, item in enumerate(weapons, start=1):
        print(f"{idx}) {item}")
    choice = int(input("Enter number: ")) - 1
    if 0 <= choice < len(weapons):
        player_data["equipped"] = weapons[choice]
        print(f"Equipped {weapons[choice]}")
    return player_data

def save_game_data(player_data):
    with open(SAVE_FILE, "w") as f:
        json.dump(player_data, f)

def load_game_data():
    with open(SAVE_FILE, "r") as f:
        return json.load(f)

def new_random_monster():
    monsters = [
        {"name": "Goblin", "description": "A sneaky goblin with a jagged blade."},
        {"name": "Slime", "description": "A sticky green blob."}
    ]
    return choice(monsters)

def handle_town_menu(player_data):
    print("\nWhat would you like to do?")
    print("1) Leave town (Explore map)")
    print("2) Sleep (Restore HP for 5 Gold)")
    print("3) Visit Shop")
    print("4) Equip Item")
    print("5) Save and Quit")
    choice = input("Enter choice (1–5): ")
    if choice == "1":
        from my_map import run_map
        return run_map(player_data)
    elif choice == "2" and player_data["gold"] >= 5:
        player_data["hp"] = 30
        player_data["gold"] -= 5
        print("Rested and healed!")
    elif choice == "3":
        player_data = purchase_item(player_data)
    elif choice == "4":
        player_data = equip_item(player_data)
    elif choice == "5":
        save_game_data(player_data)
        print("Game saved. Goodbye!")
        return "quit", player_data
    return "town", player_data
