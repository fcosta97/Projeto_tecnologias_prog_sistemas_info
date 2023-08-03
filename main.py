import pygame
from configs import *
from player import *
from world import *
from enemy import *

pygame.init()

screen = pygame.display.set_mode((Window.WIDTH, Window.HEIGHT))

pygame.display.set_caption(Window.TITLE)

clock = pygame.time.Clock()

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

    # CONTROLS
    key = pygame.key.get_pressed()

    left = key[pygame.K_a] or key[pygame.K_LEFT]
    right = key[pygame.K_d] or key[pygame.K_RIGHT]
    up = key[pygame.K_w] or key[pygame.K_UP]
    down = key[pygame.K_s] or key[pygame.K_DOWN]
    reset = key[pygame.K_r]

    if player.get_health() < 0:
        screen.blit(Game.GAME_OVER, ((Window.WIDTH / 2) - (Game.GAME_OVER.get_width() / 2),\
                                     (Window.HEIGHT / 2) - (Game.GAME_OVER.get_height() / 2)))
        
        restart = Game.FONT.render("Press R to restart", 1, (0, 0, 0)) 

        screen.blit(restart, ((Window.WIDTH / 2) - (restart.get_width() / 2),\
                                     (Window.HEIGHT / 2) - (restart.get_height() / 2) + 50))
        
        pygame.display.update()
        
        if reset:
            enemies.clear()

            player.reset()

            world.reset()
        else:
            continue

    movement = pygame.math.Vector2(right - left, down - up)

    if movement.length_squared() > 0:
        movement.scale_to_length(WorldSettings.VELOCITY * 1.5)

        x, y = round(movement.x), round(movement.y)

        if world.is_in_bounds(x, y):
            world.move(x, y)

            world.adjust_fruits(x, y)

            Enemy.adjust_group(enemies, x, y)

            player.adjust_bullets(x, y)

    for enemy in enemies:
        if player.hits(enemy):
            enemy.hurt(player.get_damage())

            if enemy.get_health() <= 0:
                enemy.drop_fruit(world)
                
                enemies.remove(enemy)

    Enemy.move_group_towards_player(enemies, player)

    enemy_timer += 1

    if enemy_timer >= Game.FPS * 4:
        enemies.extend(Enemy.create_group(random.randint(1, 4)))
        enemy_timer = 0

    score = Game.FONT_TITLE.render(F"SCORE: {player.get_score()}", 1, (0, 0, 0))

    screen.blit(score, ((Window.WIDTH / 2) - (score.get_width() / 2), 30))

    player.move_bullets()

    world.fruit_collision(player)

    player.draw_bullets(screen)

    player.draw(screen) 

    world.draw_fruits(screen)

    Enemy.draw_group(enemies, player, screen)

    pygame.display.update()

pygame.quit()