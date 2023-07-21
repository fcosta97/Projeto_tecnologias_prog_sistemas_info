import math
from configs import *
from world import *

class Bullet:
    def __init__(self, x, y, mouse_x, mouse_y):
        self.__x = x
        self.__y = y
        self.__mouse_x = mouse_x
        self.__mouse_y = mouse_y
        self.__velocity = WorldSettings.VELOCITY
        self.__angle = math.atan2(self.__y - self.__mouse_y, self.__x - self.__mouse_x)
        self.__x_vel = math.cos(self.__angle) * self.__velocity
        self.__y_vel = math.sin(self.__angle) * self.__velocity
        self.__img = Skins.BULLET

    def draw(self, surface):
        self.__x -= round(self.__x_vel)
        self.__y -= round(self.__y_vel)

        surface.blit(self.__img, [self.__x, self.__y])

    def adjust(self, x, y):
        self.__x -= x
        self.__y -= y