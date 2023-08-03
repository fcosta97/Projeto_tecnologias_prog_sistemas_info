from configs import *
from fruit import *

class WorldSettings:
    VELOCITY = 5

class WorldDirections:
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3

class World:
    def __init__(self):
        self.__background_img = Skins.BACKGROUND
        self.__bg_img_width = self.__background_img.get_width()
        self.__bg_img_height = self.__background_img.get_height()
        self.__x = (Window.WIDTH / 2) - (self.__bg_img_width / 2)
        self.__y = (Window.HEIGHT / 2) - (self.__bg_img_height / 2)
        self.__fruits = []
    
    def reset(self):
        self.__bg_img_width = self.__background_img.get_width()
        self.__bg_img_height = self.__background_img.get_height()
        self.__x = (Window.WIDTH / 2) - (self.__bg_img_width / 2)
        self.__y = (Window.HEIGHT / 2) - (self.__bg_img_height / 2)
        self.__fruits = []

    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
            
    def move(self, x, y):
        self.__x -= x 
        self.__y -= y 

        return self.__x, self.__y

    def is_in_bounds(self, x, y):
        return \
            (self.__x - x < 0 and self.__x - x > -(self.__bg_img_width - Window.WIDTH)) and \
            (self.__y - y < 0 and self.__y - y > -(self.__bg_img_height - Window.HEIGHT))
    
    def draw(self, surface):
        surface.blit(self.__background_img, (self.__x, self.__y))

    def spawn_fruit(self, x, y):
        self.__fruits.append(Fruit(x, y))

    def adjust_fruits(self, x, y):
        for fruit in self.__fruits:
            fruit.adjust(x, y)

    def draw_fruits(self, surface):
        for fruit in self.__fruits:
            fruit.draw(surface)

    def fruit_collision(self, player):
        for fruit in self.__fruits:
            if fruit.collides_with(player):
                player.eat_fruit(fruit.get_score())

                self.__fruits.remove(fruit)