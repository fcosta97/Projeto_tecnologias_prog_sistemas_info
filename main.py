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

    move = pygame.math.Vector2(right - left, down - up)

    if move.length_squared() > 0:
            
        move.scale_to_length(WorldSettings.VELOCITY)

        x, y = round(move.x), round(move.y)

        if (world.check_move_x(x) < 0 and world.check_move_x(x) > -(world.get_bg_width() - Window.WIDTH)) and (world.check_move_y(y) < 0 and world.check_move_y(y) > -(world.get_bg_height() - Window.HEIGHT)):

            world.move_ip(x, y)
        
            player.adjust_bullets(x, y)    

    # if left:
    #     world.move_left()
    #     coord_x -= world.get_velocity()

    #     player.adjust_bullets(WorldDirections.LEFT)

    # if right:
    #     world.move_right()
    #     coord_x += world.get_velocity()

    #     player.adjust_bullets(WorldDirections.RIGHT)

    # if up:
    #     world.move_up()
    #     coord_y -= world.get_velocity()

    #     player.adjust_bullets(WorldDirections.UP)

    # if down:
    #     world.move_down()
    #     coord_y += world.get_velocity()

    #     player.adjust_bullets(WorldDirections.DOWN)

    text = font.render(F"X: {coord_x}   |   Y: {coord_y}", 1, (0, 0, 0)) # for debug

    text2 = font.render(F"World X: {world.get_x()}   |   Y: {world.get_y()}", 1, (0, 0, 0)) # for debug

    screen.blit(text, (50, 50)) # for debug
    screen.blit(text2, (50, 90)) # for debug

    player.draw(screen) 
    player.draw_bullets(screen)

    pygame.display.update()

pygame.quit()