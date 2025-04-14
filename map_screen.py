import pygame
import json
import os

TILE_SIZE = 32
GRID_WIDTH = 10
GRID_HEIGHT = 10
SCREEN_WIDTH = TILE_SIZE * GRID_WIDTH
SCREEN_HEIGHT = TILE_SIZE * GRID_HEIGHT

MAP_STATE_FILE = "map_state.json"

def load_map_state():
    if os.path.exists(MAP_STATE_FILE):
        with open(MAP_STATE_FILE, "r") as f:
            return json.load(f)
    return {"player_pos": [0, 0]}  # default to top-left

def save_map_state(player_pos):
    with open(MAP_STATE_FILE, "w") as f:
        json.dump({"player_pos": player_pos}, f)

def run_map_screen():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Adventure Map")

    clock = pygame.time.Clock()

    town_pos = [0, 0]
    monster_pos = [5, 5]
    state = load_map_state()
    player_pos = state["player_pos"]

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and player_pos[1] > 0:
                    player_pos[1] -= 1
                elif event.key == pygame.K_DOWN and player_pos[1] < GRID_HEIGHT - 1:
                    player_pos[1] += 1
                elif event.key == pygame.K_LEFT and player_pos[0] > 0:
                    player_pos[0] -= 1
                elif event.key == pygame.K_RIGHT and player_pos[0] < GRID_WIDTH - 1:
                    player_pos[0] += 1

        screen.fill((0, 0, 0))

        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(screen, (255, 255, 255), rect, 1)

        tx, ty = town_pos
        pygame.draw.circle(screen, (0, 255, 0), (tx * TILE_SIZE + 16, ty * TILE_SIZE + 16), 10)

        mx, my = monster_pos
        pygame.draw.circle(screen, (255, 0, 0), (mx * TILE_SIZE + 16, my * TILE_SIZE + 16), 10)

        px, py = player_pos
        pygame.draw.rect(screen, (0, 0, 255), (px * TILE_SIZE, py * TILE_SIZE, TILE_SIZE, TILE_SIZE))

        pygame.display.flip()
        clock.tick(10)

        if player_pos == town_pos:
            save_map_state(player_pos)
            return "town", player_pos
        elif player_pos == monster_pos:
            save_map_state(player_pos)
            return "monster", player_pos
