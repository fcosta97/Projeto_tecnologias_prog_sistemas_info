from configs import *

class Bullet:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__img = Skins.BULLET

    def draw(self, surface):
        surface.blit(self.__img, [self.__x, self.__y])