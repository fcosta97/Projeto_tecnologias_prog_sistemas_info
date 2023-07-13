import pygame
pygame.init()

class Window:
    WIDTH = 1720
    HEIGHT = 988
    TITLE = "TEST"
    # ICON = pygame.image.load("imgs/icon.png")

pygame.display.set_mode((Window.WIDTH, Window.HEIGHT))

class World:
    BACKGROUND = pygame.image.load("imgs/bg.png").convert_alpha()

class Skins:
    PLAYER = pygame.image.load("imgs/player.png").convert_alpha()
    ENEMY = pygame.image.load("imgs/enemy.png").convert_alpha()
    FRUIT = pygame.image.load("imgs/fruit.png").convert_alpha()

# class Font:
    # MAIN = pygame.font.Font('fonts/Roboto-Regular.ttf', 50)