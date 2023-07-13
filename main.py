import pygame
from configs import *
from player import Player

pygame.init()

screen = pygame.display.set_mode((Window.WIDTH, Window.HEIGHT))

pygame.display.set_caption(Window.TITLE)

player = Player()

clock = pygame.time.Clock()
FPS = 60

background_x = 0
background_y = 0

while 1:
    dt = clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.blit(World.BACKGROUND, [background_x, background_y])

    key = pygame.key.get_pressed()

    if key[pygame.K_a] or key[pygame.K_LEFT]:
        # player.move_left()
        background_x -= 5
    if key[pygame.K_d] or key[pygame.K_RIGHT]:
        # player.move_right()
        background_x += 5
    if key[pygame.K_w] or key[pygame.K_UP]:
        # player.move_up()
        background_y -= 5
    if key[pygame.K_s] or key[pygame.K_DOWN]:
        # player.move_down()
        background_y += 5


    player.draw(screen)

    pygame.display.update()

pygame.quit()