import pygame
import constance as c
from particle_spawner import ParticleSpawner
import random
from Explosions import P1AsteroidExplosions

class Spin_Icon(pygame.sprite.Sprite): ##this is how the ship will look and spawn
    def __init__(self):
        super(Spin_Icon, self).__init__()
        self.image = pygame.image.load("spin_icon.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.vel_y = 1
        self.vel_x = 0
        self.rect.x = random.randrange(0, (c.display_width - self.rect.width))
        self.rect.y = -self.rect.height


    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y


class Speed_boost(pygame.sprite.Sprite):
    def __init__(self):
        super(Speed_boost, self).__init__()
        self.image = pygame.image.load("speed_icon.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.vel_y = 1
        self.vel_x = 0
        self.rect.x = random.randrange(0, (c.display_width - self.rect.width))
        self.rect.y = -self.rect.height

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

class Max_gems(pygame.sprite.Sprite):
    def __init__(self):
        super(Max_gems, self).__init__()
        self.image = pygame.image.load("max_gems.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.vel_y = 1
        self.vel_x = 0
        self.rect.x = random.randrange(0, (c.display_width - self.rect.width))
        self.rect.y = -self.rect.height

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

class Roll_Icon(pygame.sprite.Sprite): ##this is how the ship will look and spawn
    def __init__(self):
        super(Roll_Icon, self).__init__()
        self.roll_img_01 = pygame.image.load("barrel_1.png")
        self.roll_img_02 = pygame.image.load("barrel_2.png")
        self.roll_img_03 = pygame.image.load("barrel_3.png")
        self.roll_img_04 = pygame.image.load("barrel_4.png")
        self.roll_img_05 = pygame.image.load("barrel_5.png")
        self.anim_roll = [self.roll_img_01, self.roll_img_02, self.roll_img_03,
                          self.roll_img_04, self.roll_img_05]
        self.anim_index = 0
        self.frame_length_max = 10
        self.frame_length = self.frame_length_max
        self.image = self.anim_roll[self.anim_index]
        self.rect = self.image.get_rect()
        self.vel_y = 1
        self.vel_x = 0
        self.rect.x = random.randrange(0, (c.display_width - self.rect.width))
        self.rect.y = -self.rect.height


    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        max_index = len(self.anim_roll) - 1
        if self.frame_length == 0:
            self.anim_index += 1
            if self.anim_index > max_index:
                self.anim_index = 0
            else:
                self.image = self.anim_roll[self.anim_index]
                self.frame_length = self.frame_length_max
        else:
            self.frame_length -= 1

class Blue_Flame(pygame.sprite.Sprite):
    def __init__(self):
        super(Blue_Flame, self).__init__()
        self.image = pygame.image.load("flame_blue_01.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.vel_y = 1
        self.vel_x = 0
        self.rect.x = random.randrange(0, (c.display_width - self.rect.width))
        self.rect.y = -self.rect.height

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

class Red_Flame(pygame.sprite.Sprite):
    def __init__(self):
        super(Red_Flame, self).__init__()
        self.image = pygame.image.load("flame_red_01.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.vel_y = 1
        self.vel_x = 0
        self.rect.x = random.randrange(0, (c.display_width - self.rect.width))
        self.rect.y = -self.rect.height

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y