import pygame
import random

pygame.init()

screen = pygame.display.set_mode((600, 700))
clock = pygame.time.Clock()

player = pygame.Rect(275, 600, 50, 80)
enemy = pygame.Rect(random.randint(100, 450), -80, 50, 80)

score = 0
speed = 6
running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= 7
    if keys[pygame.K_RIGHT]:
        player.x += 7

    player.x = max(100, min(player.x, 450))

    enemy.y += speed

    if enemy.y > 700:
        enemy.y = -80
        enemy.x = random.randint(100, 450)
        score += 1

    if player.colliderect(enemy):
        running = False

    screen.fill((30, 150, 50))

    pygame.draw.rect(screen, (60, 60, 60), (100, 0, 400, 700))
    pygame.draw.rect(screen, (0, 100, 255), player)
    pygame.draw.rect(screen, (255, 50, 50), enemy)

    pygame.display.flip()

pygame.quit()
