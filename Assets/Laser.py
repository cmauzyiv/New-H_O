import pygame
import constance as c
image = pygame.image.load("new_laser1.png")



class LLaser(pygame.sprite.Sprite):
    def __init__(self):
        super(LLaser, self). __init__()
        self.main_image = pygame.image.load("new_laser1.png").convert_alpha()
        self.rect = self.main_image.get_rect()
        self.main_image_center = self.main_image.get_rect().center
        self.anim_01 = pygame.image.load("new_laser_01.png")
        self.anim_02 = pygame.image.load("new_laser_02.png")
        self.anim_03 = pygame.image.load("new_laser_03.png")
        self.anim_04 = pygame.image.load("new_laser_04.png")
        self.anim_05 = pygame.image.load("new_laser_05.png")
        self.anim_06 = pygame.image.load("new_laser_06.png")
        self.anim_laser = [self.anim_01, self.anim_02, self.anim_03, self.anim_04, self.anim_05, self.anim_06]
        self.anim_index = 0
        self.frame_length_max = 3
        self.frame_length = self.frame_length_max
        self.image = self.anim_laser[self.anim_index]
        self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        self.vel_x = 0
        self.vel_y = -12

    def get_image(self, x, y, width, height):
        return self.sprite_sheet.subsurface((x, y, width, height))

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        max_index = len(self.anim_laser) - 1
        if self.frame_length == 0:
            self.anim_index += 1
            if self.anim_index == 4:
                self.vel_x = 0
            if self.anim_index > max_index:
                self.anim_index = max_index
            else:
                self.image = self.anim_laser[self.anim_index]
                self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
                self.frame_length = self.frame_length_max
        else:
            self.frame_length -= 1




class RLaser(pygame.sprite.Sprite):
    def __init__(self):
        super(RLaser, self). __init__()
        self.image = pygame.image.load("llaser.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.x_pad = 10
        self.vel_x = 0
        self.vel_y = -12

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y


class LMuzzle(pygame.sprite.Sprite):
    def __init__(self):
        super(LMuzzle, self). __init__()
        self.img_muzzle_01 = pygame.image.load("muzzle1.png").convert_alpha()
        self.img_muzzle_02 = pygame.image.load("muzzle2.png").convert_alpha()
        self.img_muzzle_03 = pygame.image.load("muzzle3.png").convert_alpha()
        self.img_muzzle_04 = pygame.image.load("muzzle4.png").convert_alpha()
        self.img_muzzle_05 = pygame.image.load("muzzle5.png").convert_alpha()
        self.img_muzzle_06 = pygame.image.load("muzzle6.png").convert_alpha()


        self.anim_explosion = [self.img_muzzle_01,
                               self.img_muzzle_02,
                               self.img_muzzle_03,
                               self.img_muzzle_04,
                               self.img_muzzle_05,
                               self.img_muzzle_06]
        self.anim_index = 0
        self.frame_length_max = 3
        self.frame_length = self.frame_length_max
        self.image = self.anim_explosion[self.anim_index]
        self.rect = self.image.get_rect()
        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        max_index = len(self.anim_explosion) - 1
        if self.frame_length == 0:
            self.anim_index += 1
            if self.anim_index > max_index:
                self.kill()
            else:
                self.image = self.anim_explosion[self.anim_index]
                self.frame_length = self.frame_length_max
        else:
            self.frame_length -= 1

class RMuzzle(pygame.sprite.Sprite):
    def __init__(self):
        super(RMuzzle, self). __init__()
        self.img_muzzle_01 = pygame.image.load("muzzle1.png").convert_alpha()
        self.img_muzzle_02 = pygame.image.load("muzzle2.png").convert_alpha()
        self.img_muzzle_03 = pygame.image.load("muzzle3.png").convert_alpha()
        self.img_muzzle_04 = pygame.image.load("muzzle4.png").convert_alpha()
        self.img_muzzle_05 = pygame.image.load("muzzle5.png").convert_alpha()
        self.img_muzzle_06 = pygame.image.load("muzzle6.png").convert_alpha()

        self.anim_explosion = [self.img_muzzle_01,
                               self.img_muzzle_02,
                               self.img_muzzle_03,
                               self.img_muzzle_04,
                               self.img_muzzle_05,
                               self.img_muzzle_06]
        self.anim_index = 0
        self.frame_length_max = 3
        self.frame_length = self.frame_length_max
        self.image = self.anim_explosion[self.anim_index]
        self.rect = self.image.get_rect()
        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        max_index = len(self.anim_explosion) - 1
        if self.frame_length == 0:
            self.anim_index += 1
            if self.anim_index > max_index:
                self.kill()
            else:
                self.image = self.anim_explosion[self.anim_index]
                self.frame_length = self.frame_length_max
        else:
            self.frame_length -= 1

