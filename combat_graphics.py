
import pygame
import time
import random

def graphical_combat(monster, player):
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Combat")

    font = pygame.font.SysFont(None, 24)
    clock = pygame.time.Clock()

    running = True
    combat_log = ""
    message_timer = 0

    while player["hp"] > 0 and monster["hp"] > 0 and running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                return

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:  # Attack
                    monster["hp"] -= player["damage"]
                    combat_log = f"You hit the {monster['name']} for {player['damage']}!"
                    message_timer = pygame.time.get_ticks()

                    if monster["hp"] <= 0:
                        combat_log = f"You defeated the {monster['name']}!"
                        pygame.display.flip()
                        pygame.time.wait(1500)
                        player["gold"] += random.randint(10, 30)
                        break

                    player["hp"] -= monster["damage"]
                    if player["hp"] <= 0:
                        combat_log = f"You were defeated by the {monster['name']}."
                        pygame.display.flip()
                        pygame.time.wait(2000)
                        pygame.quit()
                        exit()

        screen.fill((50, 50, 50))

        # Draw player and monster
        pygame.draw.rect(screen, (0, 0, 255), (50, 100, 50, 50))  # Player
        pygame.draw.rect(screen, (255, 0, 0), (300, 100, 50, 50))  # Monster

        # Display HP
        player_hp_text = font.render(f"Player HP: {player['hp']}", True, (255, 255, 255))
        monster_hp_text = font.render(f"{monster['name']} HP: {monster['hp']}", True, (255, 255, 255))
        combat_text = font.render(combat_log, True, (255, 255, 0))

        screen.blit(player_hp_text, (50, 20))
        screen.blit(monster_hp_text, (250, 20))

        if pygame.time.get_ticks() - message_timer < 2000:
            screen.blit(combat_text, (50, 200))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
