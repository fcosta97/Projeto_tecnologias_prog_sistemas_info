import pygame
from configs import *

class Player:
    def __init__(self):
        self.__x = (Window.WIDTH / 2) - (Skins.PLAYER.get_width() / 2)
        self.__y = (Window.HEIGHT / 2) - (Skins.PLAYER.get_height() / 2)
        self.__img = Skins.PLAYER
        self.__health = 0
        self.__score = 0

    # def move_up(self):
    #     self.__y -= 5 

    # def move_down(self):
    #     self.__y += 5

    # def move_left(self):
    #     self.__x -= 5

    # def move_right(self):
    #     self.__x += 5

    def draw(self, surface):
        surface.blit(self.__img, [self.__x, self.__y])