
"""Main game loop"""
import json
import os
from gamefunctions import (
    print_welcome, print_shop_menu, purchase_item,
    equip_item, save_game_data, load_game_data,
    new_random_monster, handle_town_menu
)

SAVE_FILE = "save_data.json"

def start_new_game():
    player_name = input("What is your name, adventurer? ")
    player_data = {
        "name": player_name,
        "hp": 30,
        "gold": 20,
        "inventory": ["rock"],
        "equipped": None,
        "player_pos": [0, 0]
    }
    print(f"Welcome, {player_name}! Your adventure begins now.")
    return player_data

def main():
    print("Welcome to the Adventure Game!")
    print("1) Start New Game")
    print("2) Load Saved Game")
    choice = input("Enter choice: ")

    if choice == "1":
        player_data = start_new_game()
    elif choice == "2" and os.path.exists(SAVE_FILE):
        player_data = load_game_data()
    else:
        print("No save found. Starting new game.")
        player_data = start_new_game()

    print_welcome()
    while True:
        result, player_data = handle_town_menu(player_data)
        if result == "quit":
            break

if __name__ == "__main__":
    main()
