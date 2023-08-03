import math
import random
from configs import *
from world import *

class Enemy():
    def __init__(self):
        self.__x = random.choice([random.randint(-3000, -2500), random.randint(2500, 3000)])
        self.__y = random.choice([random.randint(-3000, -2500), random.randint(2500, 3000)])
        self.__img = Skins.ENEMY
        self.__health = 1
        self.__damage = 1
        self.__drops_fruit = random.randint(0, 1)

    def get_damage(self):
        return self.__damage
    
    # create group 
    @staticmethod
    def create_group(quantity):
        enemies = []

        for number in range(quantity):
            enemies.append(Enemy())

        return enemies
    
    # move towards player
    def move_towards_player(self, player):
        if self.hits(player):
            player.hurt(self.get_damage())

        direction_x = player.get_x() - self.__x

        direction_y = player.get_y() - self.__y

        distance = math.hypot(direction_x, direction_y)

        direction_x = direction_x / distance

        direction_y = direction_y / distance

        self.__x += (direction_x * WorldSettings.VELOCITY) * 0.5
        self.__y += (direction_y * WorldSettings.VELOCITY) * 0.5

    @staticmethod
    def move_group_towards_player(enemy_group, player):
        for enemy in enemy_group:
            enemy.move_towards_player(player)

    def collides_with(self, who):
        return who.get_overlaping_area(self.__img, self.__x, self.__y) > 0
    
    def get_overlaping_area(self, image, offset_x, offset_y):
        self_mask = pygame.mask.from_surface(self.__img)
        who_mask = pygame.mask.from_surface(image)
        return who_mask.overlap_area(self_mask, [self.__x - offset_x, self.__y - offset_y])
    
    def drop_fruit(self, world):
        if self.__drops_fruit:
            world.spawn_fruit(self.__x, self.__y)

    def get_health(self):
        return self.__health
    
    def hurt(self, damage):
        self.__health -= damage
    
    def hits(self, player):
        return self.collides_with(player)

    def adjust(self, x, y):
        self.__x -= x
        self.__y -= y

    @staticmethod
    def adjust_group(enemy_group, x, y):
        for enemy in enemy_group:
            enemy.adjust(x, y)

    def draw(self, player_x, player_y, surface):

        rel_x = round(player_x - self.__x)
        rel_y = round(player_y - self.__y)

        angle = round((180 / math.pi) * -math.atan2(rel_y , rel_x))
        rotated_image = pygame.transform.rotate(self.__img, angle)
        new_rect = rotated_image.get_rect(center = self.__img.get_rect(center = (self.__x, self.__y)).center)

        surface.blit(rotated_image, new_rect)

    # draw group
    def draw_group(enemy_group, player, surface):
        for enemy in enemy_group:
            enemy.draw(player.get_x(), player.get_y(), surface)

    