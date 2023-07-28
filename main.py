import pygame
from configs import *
from player import *
from world import *
from enemy import *

pygame.init()

screen = pygame.display.set_mode((Window.WIDTH, Window.HEIGHT))

pygame.display.set_caption(Window.TITLE)

clock = pygame.time.Clock()

coord_x = 0 # for debug
coord_y = 0 # for debug

font = pygame.font.SysFont(None, 24)

world = World()

player = Player()

enemies = Enemy.create_group(1)

enemy_timer = 0

while 1:
    dt = clock.tick(Game.FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                player.shoot()

    world.draw(screen)

    Enemy.move_group_towards_player(enemies, player)

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

            Enemy.adjust_group(enemies, x, y)

            player.adjust_bullets(x, y)

            coord_x += x # for debug
            coord_y += y # for debug

    for enemy in enemies:
        if not player.hits(enemy):
            continue

        enemy.hurt(player.get_damage())

        if enemy.get_health() <= 0:
            enemies.remove(enemy)
        
    enemy_timer += 1

    if enemy_timer >= Game.FPS * 4:
        enemies += Enemy.create_group(random.randint(1, 4))
        enemy_timer = 0

    text = font.render(F"X: {coord_x}   |   Y: {coord_y}", 1, (0, 0, 0)) # for debug
    text2 = font.render(F"World X: {world.get_x()}   |   World Y: {world.get_y()}", 1, (0, 0, 0)) # for debug
    text3 = font.render(F"Player health: {player.get_health()}", 1, (0, 0, 0)) # for debug
    text4 = font.render(F"Bullets: {player.get_len_bullets()}", 1, (0, 0, 0)) # for debug
    text5 = font.render(F"FPS: {round(clock.get_fps())}", 1, (0, 0, 0)) # for debug

    screen.blit(text, (50, 50)) # for debug
    screen.blit(text2, (50, 90)) # for debug
    screen.blit(text3, (50, 120)) # for debug
    screen.blit(text4, (50, 150)) # for debug
    screen.blit(text5, (50, 190)) # for debug

    player.move_bullets()
    player.draw_bullets(screen)
    player.draw(screen) 

    Enemy.draw_group(enemies, player, screen)

    pygame.display.update()

pygame.quit()