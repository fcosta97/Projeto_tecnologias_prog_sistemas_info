import pygame
from configs import *
from player import Player

pygame.init()

screen = pygame.display.set_mode((Window.WIDTH, Window.HEIGHT))

pygame.display.set_caption(Window.TITLE)

player = Player()

clock = pygame.time.Clock()
FPS = 144

# tiles = math.ceil(Window.WIDTH / World.BACKGROUND_WIDTH) + math.ceil(Window.HEIGHT / World.BACKGROUND_HEIGHT)
tiles = 2

print(tiles)

background_x = 0
background_y = 0
velocity = 3

while 1:
    dt = clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # BACKGROUND
    for i in range(0, tiles):
        screen.blit(World.BACKGROUND, (i * World.BACKGROUND_WIDTH + background_x, background_y)) # right
        screen.blit(World.BACKGROUND, (i * World.BACKGROUND_WIDTH + background_x, World.BACKGROUND_HEIGHT + background_y)) # down right
        screen.blit(World.BACKGROUND, (i * World.BACKGROUND_WIDTH + background_x, -World.BACKGROUND_HEIGHT + background_y)) # up right

        screen.blit(World.BACKGROUND, (i * -World.BACKGROUND_WIDTH + background_x, background_y)) # left
        screen.blit(World.BACKGROUND, (i * -World.BACKGROUND_WIDTH + background_x, World.BACKGROUND_HEIGHT + background_y)) # down left
        screen.blit(World.BACKGROUND, (i * -World.BACKGROUND_WIDTH + background_x, -World.BACKGROUND_HEIGHT + background_y)) # up left

    if abs(background_x) > World.BACKGROUND_WIDTH:
        background_x = 0

    if abs(background_y) > World.BACKGROUND_HEIGHT:
        background_y = 0

    # screen.blit(World.BACKGROUND, [background_x, background_y])

    # CONTROLS
    key = pygame.key.get_pressed()

    if key[pygame.K_a] or key[pygame.K_LEFT]:
        background_x += velocity
    if key[pygame.K_d] or key[pygame.K_RIGHT]:
        background_x -= velocity
    if key[pygame.K_w] or key[pygame.K_UP]:
        background_y += velocity
    if key[pygame.K_s] or key[pygame.K_DOWN]:
        background_y -= velocity

    player.draw(screen)

    pygame.display.update()

pygame.quit()