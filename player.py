import math
import pygame
from bullet import Bullet
from configs import *
from world import WorldSettings, WorldDirections

class Player:
    def __init__(self):
        self.__x = (Window.WIDTH / 2) - (Skins.PLAYER.get_width() / 2)
        self.__y = (Window.HEIGHT / 2) - (Skins.PLAYER.get_height() / 2)
        self.__img = Skins.PLAYER
        self.__sight_img = Skins.SIGHT
        self.__health = 1
        self.__score = 0
        self.__bullets = []
        self.__bullet_damage = 1

    def reset(self):
        self.__initial_x = (Window.WIDTH / 2) - (Skins.PLAYER.get_width() / 2)
        self.__x = self.__initial_x
        self.__initial_y = (Window.HEIGHT / 2) - (Skins.PLAYER.get_height() / 2)
        self.__y = self.__initial_y
        self.__health = 1
        self.__score = 0
        self.__bullets = []
        self.__bullet_damage = 1

    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
    def get_health(self):
        return self.__health
        
    def get_damage(self):
        return self.__bullet_damage
    
    def get_len_bullets(self): # for debug
        return len(self.__bullets)
    
    def get_score(self):
        return self.__score
    
    def get_overlaping_area(self, image, offset_x, offset_y):
        self_mask = pygame.mask.from_surface(self.__img)
        who_mask = pygame.mask.from_surface(image)
        return who_mask.overlap_area(self_mask, [self.__x - offset_x, self.__y - offset_y])
    
    def collides_with(self, who):
        return who.get_overlaping_area(self.__img, self.__x, self.__y) > 0
    
    def hurt(self, damage):
        self.__health -= damage

    def shoot(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        self.__bullets.append(Bullet(self.__x, self.__y, mouse_x, mouse_y))

    def adjust_bullets(self, x, y):
        for bullet in self.__bullets:
            bullet.adjust(x, y)

    def move_bullets(self):
        for bullet in self.__bullets:

            bullet.move()

            if bullet.is_out():
                self.__bullets.remove(bullet)

    def hits(self, enemy):
        for bullet in self.__bullets:
            if bullet.collides_with(enemy):                
                self.__bullets.remove(bullet)

                self.__score += 1

                return True

    def draw_bullets(self, surface):
        for bullet in self.__bullets:
                bullet.draw(surface)

    def draw(self, surface):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        offset = pygame.math.Vector2(64, 10)

        rel_x = round(mouse_x - self.__x)
        rel_y = round(mouse_y - self.__y)

        angle = round((180 / math.pi) * -math.atan2(rel_y , rel_x))

        rotated_offset = offset.rotate(-angle)  

        rotated_image = pygame.transform.rotate(self.__img, angle)

        rotated__sight_image = pygame.transform.rotate(self.__sight_img, angle)

        new_rect = rotated_image.get_rect(center = self.__img.get_rect(center = (self.__x, self.__y)).center)

        new_sight_rect = rotated__sight_image.get_rect(center = self.__img.get_rect(center = (self.__x, self.__y)).center + rotated_offset)

        surface.blit(rotated__sight_image, new_sight_rect)

        surface.blit(rotated_image, new_rect)

    def eat_fruit(self, score):
        self.__health += score
        self.__score += score