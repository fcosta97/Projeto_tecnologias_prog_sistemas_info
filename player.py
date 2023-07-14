import math
import pygame
from bullet import Bullet
from configs import *

class Player:
    def __init__(self):
        self.__x = (Window.WIDTH / 2) - (Skins.PLAYER.get_width() / 2)
        self.__y = (Window.HEIGHT / 2) - (Skins.PLAYER.get_height() / 2)
        self.__img = Skins.PLAYER
        self.__health = 0
        self.__score = 0
        self.__total_shoot_frames = 0
        self.__bullets = []

    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y

    def shoot(self):
        self.__bullets.append(Bullet(self.__x + 100, self.__y + 100))

    def shoot_if_ready(self):
        self.__total_shoot_frames += 1
        if self.__total_shoot_frames == 120:
            self.__bullets.append(Bullet(self.__x, self.__y))
            self.__total_shoot_frames = 0

    def draw_bullets(self, surface):
        for bullet in self.__bullets:
            bullet.draw(surface)

    def draw(self, surface):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        rel_x  = mouse_x - self.__x
        rel_y = mouse_y - self.__y

        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)

        rotated_image = pygame.transform.rotate(self.__img, angle)
        
        new_rect = rotated_image.get_rect(center = self.__img.get_rect(center = (self.__x, self.__y)).center)

        surface.blit(rotated_image, new_rect)