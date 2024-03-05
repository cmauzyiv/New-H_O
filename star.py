import pygame
import constance as c
import random


class Star(pygame.sprite.Sprite):
    def __init__(self):
        super(Star, self).__init__()
        self.image = pygame.image.load("stars_01.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.vel_y = -1
        self.vel_x = 0
        self.speed = 0

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
