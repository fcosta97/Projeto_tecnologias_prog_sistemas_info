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
        self.__sight_img = Skins.SIGHT
        self.__health = 1
        self.__score = 0
        self.__total_shoot_frames = 0
        self.__bullets = []
        self.__bullet_damage = 1

    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
    def get_initial_x(self):
        return self.__initial_x
    
    def get_initial_y(self):
        return self.__initial_y
    
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

# TEST
    def shoot_test(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        rel_x = round(mouse_x - self.__x)
        rel_y = round(mouse_y - self.__y)

        angle = round((180 / math.pi) * -math.atan2(rel_y , rel_x))

        offset = pygame.math.Vector2(30, 10)

        rotated_offset = offset.rotate(-angle)

        self.__bullets.append(Bullet(self.__x + rotated_offset[0], self.__y + rotated_offset[1], mouse_x, mouse_y))
# TEST

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

        # pygame.draw.line(surface, (0, 0, 0), (new_rect.center[0] + rotated_offset[0], new_rect.center[1] + rotated_offset[1]), (mouse_x, mouse_y), 2)

        surface.blit(rotated__sight_image, new_sight_rect)

        surface.blit(rotated_image, new_rect)

    def eats_fruit(self, score):
        self.__health += score
        self.__score += score