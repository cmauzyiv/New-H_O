import pygame
import constance as c
import random

class Particle(pygame.sprite.Sprite):
    def __init__(self):
        super(Particle, self).__init__()
        self.vel_x = 0
        self.vel_y = 0
        self.sprite_sheet = pygame.image.load("hit_fx_strip.png").convert_alpha()
        self.anim_1 = self.get_image(0, 0, 32, 32)
        self.anim_2 = self.get_image(32, 0, 32, 32)
        self.anim_3 = self.get_image(64, 0, 32, 32)
        self.anim_4 = self.get_image(96, 0, 32, 32)
        self.anim_5 = self.get_image(128, 0, 32, 32)
        self.anim_6 = self.get_image(160, 0, 32, 32)
        self.anim_7 = self.get_image(192, 0, 32, 32)
        self.anim_8 = self.get_image(224, 0, 32, 32)
        self.anim_9 = self.get_image(256, 0, 32, 32)
        self.hit_anim = [self.anim_1, self.anim_2, self.anim_3, self.anim_4, self.anim_5,
                         self.anim_6, self.anim_7, self.anim_8, self.anim_9]
        self.anim_index = 0
        self.frame_length_max = 5
        self.frame_length = self.frame_length_max
        self.image = self.hit_anim[self.anim_index]
        self.rect = self.image.get_rect()


    def get_image(self, x, y, width, height):
        return self.sprite_sheet.subsurface((x, y, width, height))


    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        max_index = len(self.hit_anim) - 1
        if self.frame_length == 0:
            self.anim_index += 1
            if self.anim_index > max_index:
                self.kill()
                self.anim_index = 0
            else:
                self.image = self.hit_anim[self.anim_index]
                self.frame_length = self.frame_length_max
        else:
            self.frame_length -= 1
