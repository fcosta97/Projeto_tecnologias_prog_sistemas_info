import math
from configs import *
from world import *

class Bullet:
    def __init__(self, x, y, mouse_x, mouse_y):
        self.__x = x
        self.__y = y
        self.__img = Skins.BULLET
        self.__mouse_x = mouse_x
        self.__mouse_y = mouse_y
        self.__velocity = WorldSettings.VELOCITY * 2
        self.__angle = math.atan2(self.__y - self.__mouse_y, self.__x - self.__mouse_x)
        self.__x_vel = math.cos(self.__angle) * self.__velocity
        self.__y_vel = math.sin(self.__angle) * self.__velocity
    
    def get_overlaping_area(self, image, offset_x, offset_y):
        self_mask = pygame.mask.from_surface(self.__img)
        who_mask = pygame.mask.from_surface(image)
        return who_mask.overlap_area(self_mask, [self.__x - offset_x, self.__y - offset_y])
    
    def collides_with(self, who):
        return who.get_overlaping_area(self.__img, self.__x, self.__y) > 0
    
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
    def is_out(self):
        return (self.__x < -2500 or self.__x > 2500) or (self.__y < -2500 or self.__y > 2500)

    def move(self):
        self.__x -= self.__x_vel
        self.__y -= self.__y_vel  

    def draw(self, surface):
        surface.blit(self.__img, [self.__x, self.__y])

    def adjust(self, x, y):
        self.__x -= x
        self.__y -= y