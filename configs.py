import pygame
pygame.init()

class Window:
    WIDTH = 1720
    HEIGHT = 988
    TITLE = "TEST"

class Game:
    FPS = 60
    FONT = pygame.font.SysFont("consolas", 24)
    FONT_TITLE = pygame.font.SysFont("consolas", 42)
    GAME_OVER = FONT_TITLE.render("GAME OVER", 1, (0, 0, 0))

pygame.display.set_mode((Window.WIDTH, Window.HEIGHT))

class Skins:
    PLAYER = pygame.image.load("imgs/player.png").convert_alpha()
    SIGHT = pygame.image.load("imgs/sight.png").convert_alpha()
    ENEMY = pygame.image.load("imgs/enemy.png").convert_alpha()
    FRUIT = pygame.image.load("imgs/fruit.png").convert_alpha()
    BULLET = pygame.image.load("imgs/bullet.png").convert_alpha()
    BACKGROUND = pygame.image.load("imgs/map.png").convert_alpha()