# File: gamefunctions.py
# Author: Kyle Auclair
# Date: March 30, 2025
# Description:
# Contains all supporting functions for the adventure game, including:
# - Input validation
# - Item purchasing
# - Equipping weapons
# - Using special items
# - Combat logic based on inventory and item types

import random

def print_welcome(name):
    print(f"\nWelcome, {name}! Your adventure begins now.")

def validate_menu_input(choice, min_val, max_val):
    while True:
        try:
            num = int(choice)
            if min_val <= num <= max_val:
                return num
            raise ValueError
        except ValueError:
            choice = input(f"Invalid input. Please enter a number between {min_val} and {max_val}: ")

def visit_shop(gold, inventory):
    print("\nWelcome to the shop! What would you like to buy?")
    print("1) Sword (10 gold) - Weapon")
    print("2) Rock (5 gold) - Special Item (Defeats a monster instantly)")
    print("3) Leave shop")

    choice = input("Enter choice (1–3): ")
    choice = validate_menu_input(choice, 1, 3)

    if choice == 1 and gold >= 10:
        inventory.append({
            "name": "sword",
            "type": "weapon",
            "maxDurability": 5,
            "currentDurability": 5
        })
        gold -= 10
        print("You bought a sword.")
    elif choice == 2 and gold >= 5:
        inventory.append({
            "name": "rock",
            "type": "special",
            "effect": "defeat monster instantly"
        })
        gold -= 5
        print("You bought a rock.")
    elif choice == 3:
        print("You leave the shop.")
    else:
        print("Not enough gold!")

    return gold, inventory

def equip_item(inventory):
    weapons = [item for item in inventory if item.get("type") == "weapon"]
    if not weapons:
        print("You have no weapons to equip.")
        return None

    print("\nAvailable weapons to equip:")
    for i, weapon in enumerate(weapons):
        print(f"{i + 1}) {weapon['name']} (Durability: {weapon['currentDurability']}/{weapon['maxDurability']})")

    choice = input("Select a weapon to equip: ")
    choice = validate_menu_input(choice, 1, len(weapons))

    selected = weapons[choice - 1]
    print(f"You equipped your {selected['name']}.")
    return selected

def leave_town(hp, gold, inventory, equipped_weapon):
    monster_hp = 20
    print("\nYou leave town and encounter a monster!")

    # Check for a rock (special item)
    special_item = next((item for item in inventory if item.get("type") == "special" and item.get("name") == "rock"), None)

    if special_item:
        print("You have a special item (rock). Would you like to use it?")
        print("1) Yes\n2) No")
        use_special = input("Enter choice: ")
        use_special = validate_menu_input(use_special, 1, 2)

        if use_special == 1:
            inventory.remove(special_item)
            print("You used the rock and instantly defeated the monster!")
            gold += 10
            return hp, gold, inventory

    # Start normal combat
    while monster_hp > 0 and hp > 0:
        print(f"\nYour HP: {hp} | Monster HP: {monster_hp}")
        print("1) Attack")
        print("2) Run")
        choice = input("Enter your choice (1–2): ")
        choice = validate_menu_input(choice, 1, 2)

        if choice == 1:
            # Use weapon if equipped
            if equipped_weapon:
                if equipped_weapon["currentDurability"] > 0:
                    player_damage = random.randint(8, 12)
                    equipped_weapon["currentDurability"] -= 1
                    print(f"You hit the monster for {player_damage} damage using your {equipped_weapon['name']}!")
                    if equipped_weapon["currentDurability"] == 0:
                        print(f"Your {equipped_weapon['name']} has broken!")
                else:
                    player_damage = random.randint(4, 6)
                    print(f"Your {equipped_weapon['name']} is broken! You attack with your fists.")
            else:
                player_damage = random.randint(4, 6)
                print(f"You hit the monster for {player_damage} damage.")

            monster_damage = random.randint(2, 6)
            monster_hp -= player_damage
            hp -= monster_damage
            print(f"The monster hits you for {monster_damage} damage.")
        else:
            print("You ran away and return to town.")
            return hp, gold, inventory

    if monster_hp <= 0:
        print("You defeated the monster! You earn 10 gold.")
        gold += 10
    elif hp <= 0:
        print("You were defeated and limp back to town with 10 HP.")
        hp = 10

    return hp, gold, inventory
