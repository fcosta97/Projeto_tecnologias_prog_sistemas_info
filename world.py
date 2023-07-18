from configs import *

class World:
    def __init__(self):
        self.__x = 0
        self.__y = 0
        self.__background_img = pygame.image.load("imgs/bg_4.png").convert_alpha()
        self.__bg_img_width = self.__background_img.get_width()
        self.__bg_img_height = self.__background_img.get_height()
        self.__velocity = 6
        self.__n_tiles = 2

    def draw(self, surface):
        for i in range(0, self.__n_tiles):
            surface.blit(self.__background_img, (i * self.__bg_img_width + self.__x, self.__y)) # right
            surface.blit(self.__background_img, (i * self.__bg_img_width + self.__x, self.__bg_img_height + self.__y)) # down right
            surface.blit(self.__background_img, (i * self.__bg_img_width + self.__x, -self.__bg_img_height + self.__y)) # up right

            surface.blit(self.__background_img, (i * -self.__bg_img_width + self.__x, self.__y)) # left
            surface.blit(self.__background_img, (i * -self.__bg_img_width + self.__x, self.__bg_img_height + self.__y)) # down left
            surface.blit(self.__background_img, (i * -self.__bg_img_width + self.__x, -self.__bg_img_height + self.__y)) # up left

        self.reset_coords_if_needed()

    def move_left(self):
        self.__x += self.__velocity

    def move_right(self):
        self.__x -= self.__velocity

    def move_up(self):
        self.__y += self.__velocity

    def move_down(self):
        self.__y -= self.__velocity

    def get_velocity(self):
        return self.__velocity

    def reset_coords_if_needed(self):
        if abs(self.__x) > self.__bg_img_width:
            self.__x = 0

        if abs(self.__y) > self.__bg_img_height:
            self.__y = 0