import math
import pygame
from bullet import Bullet
from configs import *
from world import WorldSettings, WorldDirections

class Player:
    def __init__(self):
        self.__initial_x = (Window.WIDTH / 2) - (Skins.PLAYER.get_width() / 2)
        self.__x = self.__initial_x
        self.__initial_y = (Window.HEIGHT / 2) - (Skins.PLAYER.get_height() / 2)
        self.__y = self.__initial_y
        self.__img = Skins.PLAYER
        self.__health = 0
        self.__score = 0
        self.__total_shoot_frames = 0
        self.__bullets = []

    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
    def get_initial_x(self):
        return self.__initial_x
    
    def get_initial_y(self):
        return self.__initial_y
    
    def move_left(self):
        if self.__x > 0:
            self.__x -= WorldSettings.VELOCITY

    def move_right(self):
        if self.__x < Window.WIDTH:
            self.__x += WorldSettings.VELOCITY

    def move_up(self):
        if self.__y > 0:
            self.__y -= WorldSettings.VELOCITY

    def move_down(self):
        if self.__y < Window.HEIGHT:
            self.__y += WorldSettings.VELOCITY

    def shoot(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        self.__bullets.append(Bullet(self.__x, self.__y, mouse_x, mouse_y))

    def adjust_bullets(self, x, y):
        for bullet in self.__bullets:
            bullet.adjust(x, y)

    def draw_bullets(self, surface):
        for bullet in self.__bullets:
            bullet.draw(surface)

    def draw(self, surface):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        rel_x = round(mouse_x - self.__x)
        rel_y = round(mouse_y - self.__y)

        angle = round((180 / math.pi) * -math.atan2(rel_y , rel_x))
        rotated_image = pygame.transform.rotate(self.__img, angle)
        new_rect = rotated_image.get_rect(center = self.__img.get_rect(center = (self.__x, self.__y)).center)

        surface.blit(rotated_image, new_rect)


    # def draw_test(self, surface):
    #     pivot = (21, 17)

    #     mouse_x, mouse_y = pygame.mouse.get_pos()

    #     rel_x = mouse_x - self.__x
    #     rel_y = mouse_y - self.__y

    #     angle = round((180 / math.pi) * -math.atan2(rel_y , rel_x))

    #     image_rect = self.__img.get_rect(topleft = (pivot[0] - self.__x, pivot[1] - self.__y))

    #     offset_center_to_pivot = pygame.math.Vector2(pivot) - image_rect.center

    #     rotated_offset = offset_center_to_pivot.rotate(angle)

    #     rotated_image_center = (pivot[0] - rotated_offset.x, pivot[1] - rotated_offset.y)

    #     rotated_image = pygame.transform.rotate(self.__img, angle)

    #     rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)

    #     surface.blit(rotated_image, rotated_image_rect)