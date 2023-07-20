import pygame
from configs import *
from player import Player
from world import World

pygame.init()

screen = pygame.display.set_mode((Window.WIDTH, Window.HEIGHT))

pygame.display.set_caption(Window.TITLE)

clock = pygame.time.Clock()
FPS = 144

coord_x = 0
coord_y = 0

font = pygame.font.SysFont(None, 24)

world = World()

player = Player()

while 1:
    dt = clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    world.draw(screen)

    # CONTROLS
    key = pygame.key.get_pressed()

    if key[pygame.K_a] or key[pygame.K_LEFT]:
        world.move_left()
        coord_x -= world.get_velocity()

    if key[pygame.K_d] or key[pygame.K_RIGHT]:
        world.move_right()
        coord_x += world.get_velocity()

    if key[pygame.K_w] or key[pygame.K_UP]:
        world.move_up()
        coord_y -= world.get_velocity()

    if key[pygame.K_s] or key[pygame.K_DOWN]:
        world.move_down()
        coord_y += world.get_velocity()

    # if key[pygame.K_1]:
        # player.shoot_if_ready()
        # player.shoot()

    text = font.render(F"X: {coord_x}   |   Y: {coord_y}", 1, (0, 0, 0)) # for debug

    text2 = font.render(F"World X: {world.get_x()}   |   Y: {world.get_y()}", 1, (0, 0, 0)) # for debug

    screen.blit(text, (50, 50)) # for debug
    screen.blit(text2, (50, 90)) # for debug

    player.draw(screen) 
    # player.draw_bullets(screen)

    pygame.display.update()

pygame.quit()