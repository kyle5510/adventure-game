
import pygame
import sys
import json
from gamefunctions import player, sleep
from combat_graphics import graphical_combat
from wanderingMonster import move_monsters

TILE_SIZE = 32
GRID_SIZE = 10
TOWN_COORDINATE = (0, 0)
MONSTER_COLOR = (255, 0, 0)
TOWN_COLOR = (0, 255, 0)

npc_interacted = False  # To track if player has already received the gift

def save_position(position):
    with open("position.json", "w") as f:
        json.dump(position, f)

def load_position():
    try:
        with open("position.json", "r") as f:
            return tuple(json.load(f))
    except FileNotFoundError:
        return (0, 0)

def npc_give_gift():
    if "potion" not in player["inventory"]:
        print("NPC: Welcome, traveler! Here, take this potion on the house.")
        player["inventory"].append("potion")
    else:
        print("NPC: Stay safe out there!")

def launch_map(monsters):
    global npc_interacted
    pygame.init()
    screen = pygame.display.set_mode((TILE_SIZE * GRID_SIZE, TILE_SIZE * GRID_SIZE))
    pygame.display.set_caption("Adventure Map")

    player_pos = load_position()
    move_counter = 0
    clock = pygame.time.Clock()

    running = True
    while running:
        screen.fill((0, 0, 0))

        # Draw grid
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                color = (200, 200, 200)
                if (x, y) == TOWN_COORDINATE:
                    color = TOWN_COLOR
                elif any(monster["position"] == (x, y) for monster in monsters):
                    color = MONSTER_COLOR
                pygame.draw.rect(screen, color, rect)

        # Draw player
        pygame.draw.rect(screen, (0, 0, 255), (player_pos[0] * TILE_SIZE, player_pos[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_position(player_pos)
                running = False
            elif event.type == pygame.KEYDOWN:
                new_pos = list(player_pos)
                if event.key == pygame.K_LEFT:
                    new_pos[0] -= 1
                elif event.key == pygame.K_RIGHT:
                    new_pos[0] += 1
                elif event.key == pygame.K_UP:
                    new_pos[1] -= 1
                elif event.key == pygame.K_DOWN:
                    new_pos[1] += 1

                if 0 <= new_pos[0] < GRID_SIZE and 0 <= new_pos[1] < GRID_SIZE:
                    player_pos = tuple(new_pos)
                    print(f"Moved to: {player_pos}")
                    move_counter += 1
                    if move_counter % 2 == 0:
                        move_monsters(monsters, TOWN_COORDINATE)

                for monster in monsters:
                    if monster["position"] == player_pos:
                        graphical_combat(monster, player)
                        monster["hp"] = 20  # Reset after battle

                if player_pos == TOWN_COORDINATE:
                    print("\nYou've entered the town!")
                    sleep()
                    if not npc_interacted:
                        npc_give_gift()
                        npc_interacted = True

        clock.tick(10)
    pygame.quit()
