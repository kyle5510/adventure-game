
"""Map handling with pygame"""
import pygame
import sys
from gamefunctions import save_game_data, load_game_data

TILE_SIZE = 32
GRID_SIZE = 10
SCREEN_SIZE = TILE_SIZE * GRID_SIZE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PLAYER_COLOR = (0, 0, 255)
TOWN_COLOR = (0, 255, 0)
MONSTER_COLOR = (255, 0, 0)

def run_map(player_data):
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
    pygame.display.set_caption("Adventure Map")
    clock = pygame.time.Clock()

    px, py = player_data["player_pos"]
    player_pos = [px, py]
    town_tile = (0, 0)
    monster_tile = (5, 5)

    running = True
    result = None

    while running:
        screen.fill(WHITE)
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(screen, BLACK, rect, 1)

        # Draw town
        town_rect = pygame.Rect(town_tile[0]*TILE_SIZE, town_tile[1]*TILE_SIZE, TILE_SIZE, TILE_SIZE)
        pygame.draw.circle(screen, TOWN_COLOR, town_rect.center, TILE_SIZE // 2 - 4)

        # Draw monster
        monster_rect = pygame.Rect(monster_tile[0]*TILE_SIZE, monster_tile[1]*TILE_SIZE, TILE_SIZE, TILE_SIZE)
        pygame.draw.circle(screen, MONSTER_COLOR, monster_rect.center, TILE_SIZE // 2 - 4)

        # Draw player
        px, py = player_pos
        player_rect = pygame.Rect(px*TILE_SIZE, py*TILE_SIZE, TILE_SIZE, TILE_SIZE)
        pygame.draw.rect(screen, PLAYER_COLOR, player_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_game_data(player_data)
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                old_pos = list(player_pos)
                if event.key == pygame.K_LEFT and px > 0:
                    px -= 1
                elif event.key == pygame.K_RIGHT and px < GRID_SIZE - 1:
                    px += 1
                elif event.key == pygame.K_UP and py > 0:
                    py -= 1
                elif event.key == pygame.K_DOWN and py < GRID_SIZE - 1:
                    py += 1

                player_pos = [px, py]
                player_data["player_pos"] = player_pos
                save_game_data(player_data)

                if player_pos != old_pos:
                    print(f"Moved to {player_pos}")

                if tuple(player_pos) == town_tile:
                    pygame.quit()
                    return "town", player_data
                elif tuple(player_pos) == monster_tile:
                    pygame.quit()
                    print("You encountered a monster!")
                    monster = {"name": "Goblin", "description": "A sneaky goblin with a jagged blade."}
                    print(f"You encountered: {monster['name']}")
                    print(monster["description"])
                    print(f"Your HP: {player_data['hp']} | Monster HP: 20")
                    print("1) Attack\n2) Run")
                    return "monster", player_data

        clock.tick(10)
