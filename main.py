import pygame
from configs import *
from player import Player

pygame.init()

screen = pygame.display.set_mode((Window.WIDTH, Window.HEIGHT))

pygame.display.set_caption(Window.TITLE)

player = Player(100, 100)

clock = pygame.time.Clock()

while 1:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.blit(World.BACKGROUND, [0, 0])

    key = pygame.key.get_pressed()

    if key[pygame.K_a] or key[pygame.K_LEFT]:
        player.move_left()
    if key[pygame.K_d] or key[pygame.K_RIGHT]:
        player.move_right()
    if key[pygame.K_w] or key[pygame.K_UP]:
        player.move_up()
    if key[pygame.K_s] or key[pygame.K_DOWN]:
        player.move_down()

    player.draw(screen)

    pygame.display.update()

pygame.quit()