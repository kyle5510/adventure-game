
import json
import random
import time

# Player stats and inventory
player = {
    "name": "Hero",
    "hp": 100,
    "max_hp": 100,
    "damage": 10,
    "gold": 100,
    "inventory": [],
    "equipped": None,
    "special_items": []
}

# Shop items
shop_items = {
    "sword": {"price": 50, "damage": 15},
    "potion": {"price": 25, "heal": 30},
    "elixir": {"price": 75, "special": True}
}

def print_welcome():
    print("Welcome to the Adventure Game!")

def print_shop_menu():
    print("\n--- Town Shop ---")
    for item, details in shop_items.items():
        print(f"{item.title()}: {details['price']} gold")

def purchase_item(item_name):
    if item_name in shop_items:
        item = shop_items[item_name]
        if player["gold"] >= item["price"]:
            player["gold"] -= item["price"]
            player["inventory"].append(item_name)
            print(f"You bought a {item_name}!")
        else:
            print("Not enough gold!")
    else:
        print("Item not found.")

def equip_item(item_name):
    if item_name in player["inventory"] and item_name in shop_items:
        player["equipped"] = item_name
        player["damage"] = shop_items[item_name]["damage"]
        print(f"You equipped the {item_name}. Damage is now {player['damage']}.")
    else:
        print("Item not in inventory or not equippable.")

def use_item(item_name):
    if item_name in player["inventory"]:
        item = shop_items.get(item_name, {})
        if "heal" in item:
            player["hp"] = min(player["max_hp"], player["hp"] + item["heal"])
            print(f"You used a {item_name} and restored HP to {player['hp']}.")
            player["inventory"].remove(item_name)
        elif item.get("special"):
            player["special_items"].append(item_name)
            print(f"You used a special item: {item_name}.")
            player["inventory"].remove(item_name)
        else:
            print("Cannot use that item.")
    else:
        print("Item not in inventory.")

def save_game(filename="savefile.json"):
    with open(filename, "w") as f:
        json.dump(player, f)
    print("Game saved.")

def load_game(filename="savefile.json"):
    global player
    try:
        with open(filename, "r") as f:
            player = json.load(f)
        print("Game loaded.")
    except FileNotFoundError:
        print("Save file not found.")

def combat(monster):
    print(f"\nA wild {monster['name']} appears!")
    while player["hp"] > 0 and monster["hp"] > 0:
        print(f"\nYour HP: {player['hp']} | {monster['name']} HP: {monster['hp']}")
        action = input("Do you want to (a)ttack or (r)un? ").lower()
        if action == 'a':
            monster["hp"] -= player["damage"]
            print(f"You deal {player['damage']} damage!")
            if monster["hp"] <= 0:
                print(f"You defeated the {monster['name']}!")
                gold_reward = random.randint(10, 30)
                player["gold"] += gold_reward
                print(f"You gained {gold_reward} gold.")
                break
            player["hp"] -= monster["damage"]
            print(f"The {monster['name']} hits you for {monster['damage']} damage!")
        elif action == 'r':
            if random.random() > 0.5:
                print("You escaped!")
                break
            else:
                print("You failed to escape!")
                player["hp"] -= monster["damage"]
        else:
            print("Invalid action.")
        time.sleep(1)
    if player["hp"] <= 0:
        print("You have been defeated. Game over.")
        exit()

def sleep():
    print("You rest and recover your strength.")
    player["hp"] = player["max_hp"]
    print(f"Your HP is restored to {player['hp']}.")
