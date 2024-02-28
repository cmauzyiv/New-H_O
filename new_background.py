import pygame, math
from star import Star
import constance as c

class NewBg(pygame.sprite.Sprite):
    def __init__(self):
        super(NewBg, self).__init__()
        self.image = pygame.image.load("bg_p1.png").convert_alpha()
        self.rect = self.image.get_rect()
        ##self.tiles = math.ceil(c.display_height // self.image.get_height()) + 1
        self.move = True
        self.stars_group = pygame.sprite.Group()
        self.vel_y = -1
        self.vel_x = 0
        self.speed = 0


    def update(self):
        self.rect.y += self.vel_y
        self.rect.x += self.vel_x




class p2NewBg(pygame.sprite.Sprite):
    def __init__(self):
        super(p2NewBg, self).__init__()
        self.image = pygame.image.load("bg_p2.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.stars_group = pygame.sprite.Group()
        self.o_pos = 300
        ##self.tiles = math.ceil(c.display_height // self.image.get_height()) + 1
        self.move = True
        self.vel_y = 1
        self.vel_x = 0
        self.speed = 0


    def update(self):
        self.rect.y -= self.vel_y
        self.rect.x += self.vel_x


class p3NewBg(pygame.sprite.Sprite):
    def __init__(self):
        super(p3NewBg, self).__init__()
        self.image = pygame.image.load("bg_03_new.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.stars_group = pygame.sprite.Group()
        self.o_pos = 300
        ##self.tiles = math.ceil(c.display_height // self.image.get_height()) + 1
        self.move = True
        self.vel_y = 1
        self.vel_x = 0
        self.speed = 0


    def update(self):
        self.rect.y -= self.vel_y
        self.rect.x += self.vel_x


class p4NewBg(pygame.sprite.Sprite):
    def __init__(self):
        super(p4NewBg, self).__init__()
        self.image = pygame.image.load("bg_p3.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.stars_group = pygame.sprite.Group()
        self.o_pos = 300
        ##self.tiles = math.ceil(c.display_height // self.image.get_height()) + 1
        self.move = True
        self.vel_y = 1
        self.vel_x = 0
        self.speed = 0


    def update(self):
        self.rect.y -= self.vel_y
        self.rect.x += self.vel_x








