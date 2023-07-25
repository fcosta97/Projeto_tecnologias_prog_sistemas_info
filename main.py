import pygame
from configs import *
from player import *
from world import *

pygame.init()

screen = pygame.display.set_mode((Window.WIDTH, Window.HEIGHT))

pygame.display.set_caption(Window.TITLE)

clock = pygame.time.Clock()

coord_x = 0 # for debug
coord_y = 0 # for debug

font = pygame.font.SysFont(None, 24)

world = World()

player = Player()

while 1:
    dt = clock.tick(Game.FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                player.shoot()

    world.draw(screen)

    # CONTROLS
    key = pygame.key.get_pressed()

    left = key[pygame.K_a] or key[pygame.K_LEFT]
    right = key[pygame.K_d] or key[pygame.K_RIGHT]
    up = key[pygame.K_w] or key[pygame.K_UP]
    down = key[pygame.K_s] or key[pygame.K_DOWN]

    #x_ajust, y_ajust = word.move(up, down, left, right)
    #return (0, 0)
    #player.adjust_bullets(x_ajust, y_ajust)

    movement = pygame.math.Vector2(right - left, down - up)

    if movement.length_squared() > 0:
        movement.scale_to_length(WorldSettings.VELOCITY)

        x, y = round(movement.x), round(movement.y)

        if world.check_move(x, y):
            world.move(x, y)

            player.adjust_bullets(x, y)

            coord_x += x # for debug
            coord_y += y # for debug

    text = font.render(F"X: {coord_x}   |   Y: {coord_y}", 1, (0, 0, 0)) # for debug
    text2 = font.render(F"World X: {world.get_x()}   |   World Y: {world.get_y()}", 1, (0, 0, 0)) # for debug

    screen.blit(text, (50, 50)) # for debug
    screen.blit(text2, (50, 90)) # for debug

    player.draw_bullets(screen)
    player.draw(screen) 

    pygame.display.update()

pygame.quit()