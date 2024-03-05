import pygame
import constance as c
import random


class Planet(pygame.sprite.Sprite):
    def __init__(self):
        super(Planet, self).__init__()
        self.planet_01 = pygame.image.load("planet_1.png").convert_alpha()
        self.planet_02 = pygame.image.load("planet_2.png").convert_alpha()
        self.planet_03 = pygame.image.load("planet_3.png").convert_alpha()
        self.planet_04 = pygame.image.load("planet_4.png").convert_alpha()
        self.planet_05 = pygame.image.load("planet_5.png").convert_alpha()
        self.img_planets = [self.planet_01,
                            self.planet_02,
                            self.planet_03,
                            self.planet_04,
                            self.planet_05]
        self.num_planets = len(self.img_planets)
        self.img_index = random.randrange(0, self.num_planets - 1)
        self.image = self.img_planets[self.img_index]
        ## that stored all images in list, got length of list, grabbing a planet from that list, then assigning that planet to image variable
        self.scale_value = random.uniform(0.25, 1.0)
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * self.scale_value),
                                            int(self.image.get_height()* self.scale_value)))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, c.display_width - self.rect.width)
        self.rect.y = 0 - self.rect.height
        self.pos_x = random.randrange(0, c.display_width - self.rect.width)
        self.pos_y = 0.0 - self.rect.height
        self.vel_x = 0
        self.vel_y = random.uniform(0.1, 1)

    def update(self):
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y
        self.rect.x = int(self.pos_x)
        self.rect.y = int(self.pos_y)
