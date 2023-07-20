from configs import *

class World:
    def __init__(self):
        self.__background_img = pygame.image.load("imgs/map_6.png").convert_alpha()
        self.__bg_img_width = self.__background_img.get_width()
        self.__bg_img_height = self.__background_img.get_height()
        self.__x = (Window.WIDTH / 2) - (self.__bg_img_width / 2)
        self.__y = (Window.HEIGHT / 2) - (self.__bg_img_height / 2)
        self.__velocity = WorldSettings.VELOCITY
        self.__n_tiles = 2

    def draw(self, surface):
        # for i in range(0, self.__n_tiles):
        #     surface.blit(self.__background_img, (i * self.__bg_img_width + self.__x, self.__y)) # right
        #     surface.blit(self.__background_img, (i * self.__bg_img_width + self.__x, self.__bg_img_height + self.__y)) # down right
        #     surface.blit(self.__background_img, (i * self.__bg_img_width + self.__x, -self.__bg_img_height + self.__y)) # up right

        #     surface.blit(self.__background_img, (i * -self.__bg_img_width + self.__x, self.__y)) # left
        #     surface.blit(self.__background_img, (i * -self.__bg_img_width + self.__x, self.__bg_img_height + self.__y)) # down left
        #     surface.blit(self.__background_img, (i * -self.__bg_img_width + self.__x, -self.__bg_img_height + self.__y)) # up left
        surface.blit(self.__background_img, (self.__x, self.__y))
        self.reset_coords_if_needed()

    def move_left(self):
        if self.is_in_bounds(WorldDirections.LEFT):
            self.__x += self.__velocity

    def move_right(self):
        if self.is_in_bounds(WorldDirections.RIGHT):
            self.__x -= self.__velocity

    def move_up(self):
        if self.is_in_bounds(WorldDirections.UP):
            self.__y += self.__velocity

    def move_down(self):
        if self.is_in_bounds(WorldDirections.DOWN):
            self.__y -= self.__velocity

    def get_velocity(self):
        return self.__velocity
    
    def get_bg_width(self):
        return self.__bg_img_width
    
    def get_bg_height(self):
        return self.get_bg_height
    
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y

    def reset_coords_if_needed(self):
        if abs(self.__x) > self.__bg_img_width:
            self.__x = 0

        if abs(self.__y) > self.__bg_img_height:
            self.__y = 0
    
    def is_in_bounds(self, direction):
        # if direction == WorldDirections.RIGHT:
        #     return self.__x >= -4680 
        
        match direction:
            case WorldDirections.LEFT:
                return self.__x <= 0 
                
            case WorldDirections.RIGHT:
                return self.__x >= -(self.__bg_img_width - Window.WIDTH) # -4680 

            case WorldDirections.UP:
                return self.__y <= 0

            case WorldDirections.DOWN:
                return self.__y >= -(self.__bg_img_height - Window.HEIGHT) # -5412 

class WorldSettings:
    VELOCITY = 5

class WorldDirections:
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3