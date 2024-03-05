import pygame

class ShipShield(pygame.sprite.Sprite):
    def __init__(self):
        super(ShipShield, self).__init__()
        self.img_explosion_01 = pygame.image.load("shield1.png").convert_alpha()
        self.img_explosion_02 = pygame.image.load("shield2.png").convert_alpha()
        self.img_explosion_03 = pygame.image.load("shield3.png").convert_alpha()
        self.img_explosion_04 = pygame.image.load("shield4.png").convert_alpha()
        self.img_explosion_05 = pygame.image.load("shield5.png").convert_alpha()
        self.img_explosion_06 = pygame.image.load("shield6.png").convert_alpha()


        self.anim_explosion = [self.img_explosion_01,
                               self.img_explosion_02,
                               self.img_explosion_03,
                               self.img_explosion_04,
                               self.img_explosion_05,
                               self.img_explosion_06]
        self.anim_index = 0
        self.frame_length_max = 7
        self.frame_length = self.frame_length_max
        self.image = self.anim_explosion[self.anim_index]
        self.rect = self.image.get_rect()
        self.kill_timer = 10
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


class TGShield(pygame.sprite.Sprite):
    def __init__(self):
        super(TGShield, self).__init__()
        self.img_explosion_01 = pygame.image.load("tg_shield1.png").convert_alpha()
        self.img_explosion_02 = pygame.image.load("tg_shield2.png").convert_alpha()
        self.img_explosion_03 = pygame.image.load("tg_shield3.png").convert_alpha()
        self.img_explosion_04 = pygame.image.load("tg_shield4.png").convert_alpha()
        self.img_explosion_05 = pygame.image.load("tg_shield5.png").convert_alpha()
        self.img_explosion_06 = pygame.image.load("tg_shield6.png").convert_alpha()


        self.anim_explosion = [self.img_explosion_01,
                               self.img_explosion_02,
                               self.img_explosion_03,
                               self.img_explosion_04,
                               self.img_explosion_05,
                               self.img_explosion_06]
        self.anim_index = 0
        self.frame_length_max = 7
        self.frame_length = self.frame_length_max
        self.image = self.anim_explosion[self.anim_index]
        self.rect = self.image.get_rect()
        self.kill_timer = 10
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


class AltShield(pygame.sprite.Sprite):
    def __init__(self):
        super(AltShield, self).__init__()
        self.img_explosion_01 = pygame.image.load("alt_shield1.png").convert_alpha()
        self.img_explosion_02 = pygame.image.load("alt_shield2.png").convert_alpha()
        self.img_explosion_03 = pygame.image.load("alt_shield3.png").convert_alpha()
        self.img_explosion_04 = pygame.image.load("alt_shield4.png").convert_alpha()
        self.img_explosion_05 = pygame.image.load("alt_shield5.png").convert_alpha()


        self.anim_explosion = [self.img_explosion_01,
                               self.img_explosion_02,
                               self.img_explosion_03,
                               self.img_explosion_04,
                               self.img_explosion_05]
        self.anim_index = 0
        self.frame_length_max = 7
        self.frame_length = self.frame_length_max
        self.image = self.anim_explosion[self.anim_index]
        self.rect = self.image.get_rect()
        self.kill_timer = 10
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


