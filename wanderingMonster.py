"""
Author: Kyle Auclair
Date: April 18th, 2025
"""

import random

GRID_SIZE = 10
TOWN_COORDINATE = (0, 0)

class WanderingMonster:
    """
    A class to represent a wandering monster on the map.
    """
    def __init__(self, monster_type):
        self.monster_type = monster_type
        self.name = self.generate_name(monster_type)
        self.color = self.get_color(monster_type)
        self.position = self.random_start_position()
        self.gold = random.randint(10, 50)

    def generate_name(self, mtype):
        return {
            'zombie': 'Undead Lurker',
            'slime': 'Gooey Blob',
            'goblin': 'Sneaky Stabber'
        }.get(mtype, 'Wandering Beast')

    def get_color(self, mtype):
        return {
            'zombie': (255, 0, 0),
            'slime': (0, 255, 0),
            'goblin': (0, 0, 255)
        }.get(mtype, (200, 200, 200))

    def random_start_position(self):
        while True:
            x = random.randint(0, GRID_SIZE - 1)
            y = random.randint(0, GRID_SIZE - 1)
            if (x, y) != TOWN_COORDINATE:
                return (x, y)

    def move(self):
        dx, dy = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])
        new_x = max(0, min(GRID_SIZE - 1, self.position[0] + dx))
        new_y = max(0, min(GRID_SIZE - 1, self.position[1] + dy))
        if (new_x, new_y) != TOWN_COORDINATE:
            self.position = (new_x, new_y)

    def to_dict(self):
        return {
            'monster_type': self.monster_type,
            'name': self.name,
            'color': self.color,
            'position': self.position,
            'gold': self.gold
        }

    @staticmethod
    def from_dict(data):
        monster = WanderingMonster(data['monster_type'])
        monster.name = data['name']
        monster.color = tuple(data['color'])
        monster.position = tuple(data['position'])
        monster.gold = data['gold']
        return monster
