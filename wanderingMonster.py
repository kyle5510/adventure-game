
import random

GRID_SIZE = 10

def initialize_monsters():
    return [
        {"name": "Slime", "hp": 20, "damage": 5, "position": (3, 3)},
        {"name": "Bat", "hp": 20, "damage": 6, "position": (6, 6)}
    ]

def move_monsters(monsters, town_pos):
    for monster in monsters:
        x, y = monster["position"]
        dx, dy = random.choice([(0,1),(0,-1),(1,0),(-1,0)])
        new_x, new_y = x + dx, y + dy

        if 0 <= new_x < GRID_SIZE and 0 <= new_y < GRID_SIZE and (new_x, new_y) != town_pos:
            monster["position"] = (new_x, new_y)
