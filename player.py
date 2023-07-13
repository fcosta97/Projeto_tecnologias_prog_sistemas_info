import math
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

    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y

    def draw(self, surface):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.__x, mouse_y - self.__y
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)

        rotated_image = pygame.transform.rotate(self.__img, angle)
        new_rect = rotated_image.get_rect(center = self.__img.get_rect(center = (self.__x, self.__y)).center)

        surface.blit(rotated_image, new_rect)