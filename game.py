"""
Author: Kyle Auclair
Date: April 18th, 2025
"""

import json
from gamefunctions import main_game_loop
from map_screen import open_map_screen

def load_game():
    try:
        with open('save_data.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_game(data):
    with open('save_data.json', 'w') as f:
        json.dump(data, f)

def main():
    data = load_game()
    while True:
        print("\nWelcome to the Adventure Game!")
        print("1. Enter the Map")
        print("2. Quit")
        choice = input("Choose an option: ")
        if choice == '1':
            data = open_map_screen(data)
            save_game(data)
        elif choice == '2':
            print("Thanks for playing!")
            break
        else:
            print("Invalid input. Try again.")

if __name__ == "__main__":
    main()
