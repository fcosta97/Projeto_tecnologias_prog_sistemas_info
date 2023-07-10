import pygame
pygame.init()

class Window:
    WIDTH = 1000
    HEIGHT = 750
    TITLE = "TEST"
    # ICON = pygame.image.load("imgs/icon.png")

class World:
    BACKGROUND = pygame.image.load("imgs/bg.png")

class Skins:
    PLAYER = pygame.image.load("imgs/player.png")
    ENEMY = pygame.image.load("imgs/enemy.png")
    FRUIT = pygame.image.load("imgs/fruit.png")

# class Font:
    # MAIN = pygame.font.Font('fonts/Roboto-Regular.ttf', 50)