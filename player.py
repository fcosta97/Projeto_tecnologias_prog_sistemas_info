import pygame
from configs import *

class Player:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__img = Skins.PLAYER
        self.__health = 0
        self.__score = 0

    def move_up(self):
        self.__y -= 5 

    def move_down(self):
        self.__y += 5

    def move_left(self):
        self.__x -= 5

    def move_right(self):
        self.__x += 5

    def draw(self, surface):
        surface.blit(self.__img, [self.__x, self.__y])