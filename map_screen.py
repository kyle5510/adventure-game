"""
Author: Kyle Auclair
Date: April 18th, 2025
"""

import pygame
import random
from wanderingMonster import WanderingMonster
from gamefunctions import main_game_loop

GRID_SIZE = 10
TILE_SIZE = 32
TOWN_COORD = (0, 0)

def open_map_screen(data):
    pygame.init()
    screen = pygame.display.set_mode((GRID_SIZE * TILE_SIZE, GRID_SIZE * TILE_SIZE))
    pygame.display.set_caption("Adventure Map")

    player_pos = data.get('player_pos', [0, 0])
    monster_data = data.get('monsters', [])
    monsters = [WanderingMonster.from_dict(m) for m in monster_data] if monster_data else [
        WanderingMonster('zombie'),
        WanderingMonster('slime')
    ]

    move_counter = 0
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill((255, 255, 255))

        pygame.draw.rect(screen, (0, 255, 0), (TOWN_COORD[0]*TILE_SIZE, TOWN_COORD[1]*TILE_SIZE, TILE_SIZE, TILE_SIZE))
        for monster in monsters:
            pygame.draw.circle(screen, monster.color, (monster.position[0]*TILE_SIZE + TILE_SIZE//2, monster.position[1]*TILE_SIZE + TILE_SIZE//2), TILE_SIZE//2)

        pygame.draw.rect(screen, (0, 0, 255), (player_pos[0]*TILE_SIZE, player_pos[1]*TILE_SIZE, TILE_SIZE, TILE_SIZE))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                dx, dy = 0, 0
                if event.key == pygame.K_UP: dy = -1
                elif event.key == pygame.K_DOWN: dy = 1
                elif event.key == pygame.K_LEFT: dx = -1
                elif event.key == pygame.K_RIGHT: dx = 1

                new_x = max(0, min(GRID_SIZE - 1, player_pos[0] + dx))
                new_y = max(0, min(GRID_SIZE - 1, player_pos[1] + dy))
                player_pos = [new_x, new_y]

                move_counter += 1
                if move_counter % 2 == 0:
                    for monster in monsters:
                        monster.move()

                for monster in monsters:
                    if tuple(player_pos) == monster.position:
                        pygame.quit()
                        main_game_loop({}, monster.to_dict())
                        running = False
                        break

        clock.tick(10)

    pygame.quit()
    data['player_pos'] = player_pos
    data['monsters'] = [m.to_dict() for m in monsters]
    return data
