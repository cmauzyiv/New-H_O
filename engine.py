import pygame
import constance as c
import random

class LEngines(pygame.sprite.Sprite):
    def __init__(self):
        super(LEngines, self).__init__()
        self.img_explosion_01 = pygame.image.load("engine1.png").convert_alpha()
        self.img_explosion_01 = pygame.transform.rotate(self.img_explosion_01, -30)
        self.img_explosion_02 = pygame.image.load("engine2.png").convert_alpha()
        self.img_explosion_02 = pygame.transform.rotate(self.img_explosion_02, -30)
        self.img_explosion_03 = pygame.image.load("engine3.png").convert_alpha()
        self.img_explosion_03 = pygame.transform.rotate(self.img_explosion_03, -30)
        self.img_explosion_04 = pygame.image.load("engine4.png").convert_alpha()
        self.img_explosion_04 = pygame.transform.rotate(self.img_explosion_04, -30)
        self.img_explosion_05 = pygame.image.load("engine5.png").convert_alpha()
        self.img_explosion_05 = pygame.transform.rotate(self.img_explosion_05, -30)

        self.anim_explosion = [self.img_explosion_01,
                               self.img_explosion_02,
                               self.img_explosion_03,
                               self.img_explosion_04,
                               self.img_explosion_05]
        self.transformed_anim_lengine = []
        for img in self.anim_explosion:
            self.transformed_anim_lengine.append(
                pygame.transform.scale(img, (img.get_width() - 15, img.get_height() - 15)))
        self.anim_index = 0
        self.frame_length_max = 5
        self.frame_length = self.frame_length_max
        self.image = self.transformed_anim_lengine[self.anim_index]
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
                self.anim_index = 0
            else:
                self.image = self.transformed_anim_lengine[self.anim_index]
                self.frame_length = self.frame_length_max
        else:
            self.frame_length -= 1

class LFlames(pygame.sprite.Sprite):
    def __init__(self):
        super(LFlames, self).__init__()
        self.img_flame_01 = pygame.image.load("flame_fx_blue_01.png").convert_alpha()
        self.img_flame_01 = pygame.transform.rotate(self.img_flame_01, -30)
        self.img_flame_02 = pygame.image.load("flame_fx_blue_02.png").convert_alpha()
        self.img_flame_02 = pygame.transform.rotate(self.img_flame_02, -30)
        self.img_flame_03 = pygame.image.load("flame_fx_blue_03.png").convert_alpha()
        self.img_flame_03 = pygame.transform.rotate(self.img_flame_03, -30)
        self.img_flame_04 = pygame.image.load("flame_fx_blue_04.png").convert_alpha()
        self.img_flame_04 = pygame.transform.rotate(self.img_flame_04, -30)
        self.img_flame_05 = pygame.image.load("flame_fx_blue_05.png").convert_alpha()
        self.img_flame_05 = pygame.transform.rotate(self.img_flame_05, -30)
        self.img_flame_06 = pygame.image.load("flame_fx_blue_06.png").convert_alpha()
        self.img_flame_06 = pygame.transform.rotate(self.img_flame_06, -30)
        self.img_flame_07 = pygame.image.load("flame_fx_blue_07.png").convert_alpha()
        self.img_flame_07 = pygame.transform.rotate(self.img_flame_07, -30)
        self.img_flame_08 = pygame.image.load("flame_fx_blue_08.png").convert_alpha()
        self.img_flame_08 = pygame.transform.rotate(self.img_flame_08, -30)
        self.img_flame_09 = pygame.image.load("flame_fx_blue_09.png").convert_alpha()
        self.img_flame_09 = pygame.transform.rotate(self.img_flame_09, -30)
        self.img_flame_010 = pygame.image.load("flame_fx_blue_10.png").convert_alpha()
        self.img_flame_010 = pygame.transform.rotate(self.img_flame_010, -30)
        self.img_flame_011 = pygame.image.load("flame_fx_blue_11.png").convert_alpha()
        self.img_flame_011 = pygame.transform.rotate(self.img_flame_011, -30)
        self.img_flame_012 = pygame.image.load("flame_fx_blue_12.png").convert_alpha()
        self.img_flame_012 = pygame.transform.rotate(self.img_flame_012, -30)
        self.img_flame_013 = pygame.image.load("flame_fx_blue_13.png").convert_alpha()
        self.img_flame_013 = pygame.transform.rotate(self.img_flame_013, -30)

        self.anim_lflame = [self.img_flame_01, self.img_flame_02, self.img_flame_03, self.img_flame_04,
                            self.img_flame_05, self.img_flame_06, self.img_flame_07, self.img_flame_08,
                            self.img_flame_09, self.img_flame_010, self.img_flame_011, self.img_flame_012,
                            self.img_flame_013]

        self.transformed_anim_lflame = []
        for img in self.anim_lflame:
            self.transformed_anim_lflame.append(
                pygame.transform.scale(img, (img.get_width() - 15, img.get_height() - 15)))
        self.anim_index = 0
        self.frame_length_max = 10
        self.frame_length = self.frame_length_max
        self.image = self.transformed_anim_lflame[self.anim_index]
        self.rect = self.image.get_rect()
        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        max_index = len(self.anim_lflame) - 1
        if self.frame_length == 0:
            self.anim_index += 1
            if self.anim_index > max_index:
                self.anim_index = 0
            else:
                self.image = self.transformed_anim_lflame[self.anim_index]
                self.frame_length = self.frame_length_max
        else:
            self.frame_length -= 1



class REngines(pygame.sprite.Sprite):
    def __init__(self):
        super(REngines, self).__init__()
        self.img_explosion_01 = pygame.image.load("engine1.png").convert_alpha()
        self.img_explosion_01 = pygame.transform.rotate(self.img_explosion_01, 30)
        self.img_explosion_02 = pygame.image.load("engine2.png").convert_alpha()
        self.img_explosion_02 = pygame.transform.rotate(self.img_explosion_02, 30)
        self.img_explosion_03 = pygame.image.load("engine3.png").convert_alpha()
        self.img_explosion_03 = pygame.transform.rotate(self.img_explosion_03, 30)
        self.img_explosion_04 = pygame.image.load("engine4.png").convert_alpha()
        self.img_explosion_04 = pygame.transform.rotate(self.img_explosion_04, 30)
        self.img_explosion_05 = pygame.image.load("engine5.png").convert_alpha()
        self.img_explosion_05 = pygame.transform.rotate(self.img_explosion_05, 30)

        self.anim_explosion = [self.img_explosion_01,
                               self.img_explosion_02,
                               self.img_explosion_03,
                               self.img_explosion_04,
                               self.img_explosion_05]
        self.transformed_anim_rengine = []
        for img in self.anim_explosion:
            self.transformed_anim_rengine.append(
                pygame.transform.scale(img, (img.get_width() - 15, img.get_height() - 15)))
        self.anim_index = 0
        self.frame_length_max = 5
        self.frame_length = self.frame_length_max
        self.image = self.transformed_anim_rengine[self.anim_index]
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
                self.anim_index = 0
            else:
                self.image = self.transformed_anim_rengine[self.anim_index]
                self.frame_length = self.frame_length_max
        else:
            self.frame_length -= 1

class RFlames(pygame.sprite.Sprite):
    def __init__(self):
        super(RFlames, self).__init__()
        self.img_flame_01 = pygame.image.load("flame_fx_blue_01.png").convert_alpha()
        self.img_flame_01 = pygame.transform.rotate(self.img_flame_01, 30)
        self.img_flame_02 = pygame.image.load("flame_fx_blue_02.png").convert_alpha()
        self.img_flame_02 = pygame.transform.rotate(self.img_flame_02, 30)
        self.img_flame_03 = pygame.image.load("flame_fx_blue_03.png").convert_alpha()
        self.img_flame_03 = pygame.transform.rotate(self.img_flame_03, 30)
        self.img_flame_04 = pygame.image.load("flame_fx_blue_04.png").convert_alpha()
        self.img_flame_04 = pygame.transform.rotate(self.img_flame_04, 30)
        self.img_flame_05 = pygame.image.load("flame_fx_blue_05.png").convert_alpha()
        self.img_flame_05 = pygame.transform.rotate(self.img_flame_05, 30)
        self.img_flame_06 = pygame.image.load("flame_fx_blue_06.png").convert_alpha()
        self.img_flame_06 = pygame.transform.rotate(self.img_flame_06, 30)
        self.img_flame_07 = pygame.image.load("flame_fx_blue_07.png").convert_alpha()
        self.img_flame_07 = pygame.transform.rotate(self.img_flame_07, 30)
        self.img_flame_08 = pygame.image.load("flame_fx_blue_08.png").convert_alpha()
        self.img_flame_08 = pygame.transform.rotate(self.img_flame_08, 30)
        self.img_flame_09 = pygame.image.load("flame_fx_blue_09.png").convert_alpha()
        self.img_flame_09 = pygame.transform.rotate(self.img_flame_09, 30)
        self.img_flame_010 = pygame.image.load("flame_fx_blue_10.png").convert_alpha()
        self.img_flame_010 = pygame.transform.rotate(self.img_flame_010, 30)
        self.img_flame_011 = pygame.image.load("flame_fx_blue_11.png").convert_alpha()
        self.img_flame_011 = pygame.transform.rotate(self.img_flame_011, 30)
        self.img_flame_012 = pygame.image.load("flame_fx_blue_12.png").convert_alpha()
        self.img_flame_012 = pygame.transform.rotate(self.img_flame_012, 30)
        self.img_flame_013 = pygame.image.load("flame_fx_blue_13.png").convert_alpha()
        self.img_flame_013 = pygame.transform.rotate(self.img_flame_013, 30)

        self.anim_rflame = [self.img_flame_01, self.img_flame_02, self.img_flame_03, self.img_flame_04,
                            self.img_flame_05, self.img_flame_06, self.img_flame_07, self.img_flame_08,
                            self.img_flame_09, self.img_flame_010, self.img_flame_011, self.img_flame_012,
                            self.img_flame_013]

        self.transformed_anim_rflame = []
        for img in self.anim_rflame:
            self.transformed_anim_rflame.append(
                pygame.transform.scale(img, (img.get_width() - 15, img.get_height() - 15)))
        self.anim_index = 0
        self.frame_length_max = 10
        self.frame_length = self.frame_length_max
        self.image = self.transformed_anim_rflame[self.anim_index]
        self.rect = self.image.get_rect()
        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        max_index = len(self.anim_rflame) - 1
        if self.frame_length == 0:
            self.anim_index += 1
            if self.anim_index > max_index:
                self.anim_index = 0
            else:
                self.image = self.transformed_anim_rflame[self.anim_index]
                self.frame_length = self.frame_length_max
        else:
            self.frame_length -= 1


class LEngines_Red(pygame.sprite.Sprite):
    def __init__(self):
        super(LEngines_Red, self).__init__()
        self.img_explosion_01 = pygame.image.load("red_engine1.png").convert_alpha()
        self.img_explosion_01 = pygame.transform.rotate(self.img_explosion_01, -30)
        self.img_explosion_02 = pygame.image.load("red_engine2.png").convert_alpha()
        self.img_explosion_02 = pygame.transform.rotate(self.img_explosion_02, -30)
        self.img_explosion_03 = pygame.image.load("red_engine3.png").convert_alpha()
        self.img_explosion_03 = pygame.transform.rotate(self.img_explosion_03, -30)
        self.img_explosion_04 = pygame.image.load("red_engine4.png").convert_alpha()
        self.img_explosion_04 = pygame.transform.rotate(self.img_explosion_04, -30)
        self.img_explosion_05 = pygame.image.load("red_engine5.png").convert_alpha()
        self.img_explosion_05 = pygame.transform.rotate(self.img_explosion_05, -30)

        self.anim_explosion = [self.img_explosion_01,
                               self.img_explosion_02,
                               self.img_explosion_03,
                               self.img_explosion_04,
                               self.img_explosion_05]
        self.transformed_anim_lengine = []
        for img in self.anim_explosion:
            self.transformed_anim_lengine.append(pygame.transform.scale(img, (img.get_width() - 15, img.get_height() - 15)))
        self.anim_index = 0
        self.frame_length_max = 5
        self.frame_length = self.frame_length_max
        self.image = self.transformed_anim_lengine[self.anim_index]
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
                self.anim_index = 0
            else:
                self.image = self.transformed_anim_lengine[self.anim_index]
                self.frame_length = self.frame_length_max
        else:
            self.frame_length -= 1

class LFlames_Red(pygame.sprite.Sprite):
    def __init__(self):
        super(LFlames_Red, self).__init__()
        self.img_flame_01 = pygame.image.load("flame_fx_red_01.png").convert_alpha()
        self.img_flame_01 = pygame.transform.rotate(self.img_flame_01, -30)
        self.img_flame_02 = pygame.image.load("flame_fx_red_02.png").convert_alpha()
        self.img_flame_02 = pygame.transform.rotate(self.img_flame_02, -30)
        self.img_flame_03 = pygame.image.load("flame_fx_red_03.png").convert_alpha()
        self.img_flame_03 = pygame.transform.rotate(self.img_flame_03, -30)
        self.img_flame_04 = pygame.image.load("flame_fx_red_04.png").convert_alpha()
        self.img_flame_04 = pygame.transform.rotate(self.img_flame_04, -30)
        self.img_flame_05 = pygame.image.load("flame_fx_red_05.png").convert_alpha()
        self.img_flame_05 = pygame.transform.rotate(self.img_flame_05, -30)
        self.img_flame_06 = pygame.image.load("flame_fx_red_06.png").convert_alpha()
        self.img_flame_06 = pygame.transform.rotate(self.img_flame_06, -30)
        self.img_flame_07 = pygame.image.load("flame_fx_red_07.png").convert_alpha()
        self.img_flame_07 = pygame.transform.rotate(self.img_flame_07, -30)
        self.img_flame_08 = pygame.image.load("flame_fx_red_08.png").convert_alpha()
        self.img_flame_08 = pygame.transform.rotate(self.img_flame_08, -30)
        self.img_flame_09 = pygame.image.load("flame_fx_red_09.png").convert_alpha()
        self.img_flame_09 = pygame.transform.rotate(self.img_flame_09, -30)
        self.img_flame_010 = pygame.image.load("flame_fx_red_10.png").convert_alpha()
        self.img_flame_010 = pygame.transform.rotate(self.img_flame_010, -30)
        self.img_flame_011 = pygame.image.load("flame_fx_red_11.png").convert_alpha()
        self.img_flame_011 = pygame.transform.rotate(self.img_flame_011, -30)
        self.img_flame_012 = pygame.image.load("flame_fx_red_12.png").convert_alpha()
        self.img_flame_012 = pygame.transform.rotate(self.img_flame_012, -30)
        self.img_flame_013 = pygame.image.load("flame_fx_red_13.png").convert_alpha()
        self.img_flame_013 = pygame.transform.rotate(self.img_flame_013, -30)

        self.anim_lflame = [self.img_flame_01, self.img_flame_02, self.img_flame_03, self.img_flame_04,
                            self.img_flame_05, self.img_flame_06, self.img_flame_07, self.img_flame_08,
                            self.img_flame_09, self.img_flame_010, self.img_flame_011, self.img_flame_012,
                            self.img_flame_013]
        self.transformed_anim_lfame = []
        for img in self.anim_lflame:
            self.transformed_anim_lfame.append(pygame.transform.scale(img, (img.get_width() - 15, img.get_height() - 15)))

        self.anim_index = 0
        self.frame_length_max = 10
        self.frame_length = self.frame_length_max
        self.image = self.transformed_anim_lfame[self.anim_index]
        self.rect = self.image.get_rect()
        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        max_index = len(self.anim_lflame) - 1
        if self.frame_length == 0:
            self.anim_index += 1
            if self.anim_index > max_index:
                self.anim_index = 0
            else:
                self.image = self.transformed_anim_lfame[self.anim_index]
                self.frame_length = self.frame_length_max
        else:
            self.frame_length -= 1



class REngines_Red(pygame.sprite.Sprite):
    def __init__(self):
        super(REngines_Red, self).__init__()
        self.img_explosion_01 = pygame.image.load("red_engine1.png").convert_alpha()
        self.img_explosion_01 = pygame.transform.rotate(self.img_explosion_01, 30)
        self.img_explosion_02 = pygame.image.load("red_engine2.png").convert_alpha()
        self.img_explosion_02 = pygame.transform.rotate(self.img_explosion_02, 30)
        self.img_explosion_03 = pygame.image.load("red_engine3.png").convert_alpha()
        self.img_explosion_03 = pygame.transform.rotate(self.img_explosion_03, 30)
        self.img_explosion_04 = pygame.image.load("red_engine4.png").convert_alpha()
        self.img_explosion_04 = pygame.transform.rotate(self.img_explosion_04, 30)
        self.img_explosion_05 = pygame.image.load("red_engine5.png").convert_alpha()
        self.img_explosion_05 = pygame.transform.rotate(self.img_explosion_05, 30)

        self.anim_explosion = [self.img_explosion_01,
                               self.img_explosion_02,
                               self.img_explosion_03,
                               self.img_explosion_04,
                               self.img_explosion_05]
        self.transformed_anim_rengine = []
        for img in self.anim_explosion:
            self.transformed_anim_rengine.append(pygame.transform.scale(img, (img.get_width() - 15, img.get_height() - 15)))
        self.anim_index = 0
        self.frame_length_max = 5
        self.frame_length = self.frame_length_max
        self.image = self.transformed_anim_rengine[self.anim_index]
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
                self.anim_index = 0
            else:
                self.image = self.transformed_anim_rengine[self.anim_index]
                self.frame_length = self.frame_length_max
        else:
            self.frame_length -= 1

class RFlames_Red(pygame.sprite.Sprite):
    def __init__(self):
        super(RFlames_Red, self).__init__()
        self.img_flame_01 = pygame.image.load("flame_fx_red_01.png").convert_alpha()
        self.img_flame_01 = pygame.transform.rotate(self.img_flame_01, 30)
        self.img_flame_02 = pygame.image.load("flame_fx_red_02.png").convert_alpha()
        self.img_flame_02 = pygame.transform.rotate(self.img_flame_02, 30)
        self.img_flame_03 = pygame.image.load("flame_fx_red_03.png").convert_alpha()
        self.img_flame_03 = pygame.transform.rotate(self.img_flame_03, 30)
        self.img_flame_04 = pygame.image.load("flame_fx_red_04.png").convert_alpha()
        self.img_flame_04 = pygame.transform.rotate(self.img_flame_04, 30)
        self.img_flame_05 = pygame.image.load("flame_fx_red_05.png").convert_alpha()
        self.img_flame_05 = pygame.transform.rotate(self.img_flame_05, 30)
        self.img_flame_06 = pygame.image.load("flame_fx_red_06.png").convert_alpha()
        self.img_flame_06 = pygame.transform.rotate(self.img_flame_06, 30)
        self.img_flame_07 = pygame.image.load("flame_fx_red_07.png").convert_alpha()
        self.img_flame_07 = pygame.transform.rotate(self.img_flame_07, 30)
        self.img_flame_08 = pygame.image.load("flame_fx_red_08.png").convert_alpha()
        self.img_flame_08 = pygame.transform.rotate(self.img_flame_08, 30)
        self.img_flame_09 = pygame.image.load("flame_fx_red_09.png").convert_alpha()
        self.img_flame_09 = pygame.transform.rotate(self.img_flame_09, 30)
        self.img_flame_010 = pygame.image.load("flame_fx_red_10.png").convert_alpha()
        self.img_flame_010 = pygame.transform.rotate(self.img_flame_010, 30)
        self.img_flame_011 = pygame.image.load("flame_fx_red_11.png").convert_alpha()
        self.img_flame_011 = pygame.transform.rotate(self.img_flame_011, 30)
        self.img_flame_012 = pygame.image.load("flame_fx_red_12.png").convert_alpha()
        self.img_flame_012 = pygame.transform.rotate(self.img_flame_012, 30)
        self.img_flame_013 = pygame.image.load("flame_fx_red_13.png").convert_alpha()
        self.img_flame_013 = pygame.transform.rotate(self.img_flame_013, 30)

        self.anim_rflame = [self.img_flame_01, self.img_flame_02, self.img_flame_03, self.img_flame_04,
                            self.img_flame_05, self.img_flame_06, self.img_flame_07, self.img_flame_08,
                            self.img_flame_09, self.img_flame_010, self.img_flame_011, self.img_flame_012,
                            self.img_flame_013]

        self.transformed_anim_rflame = []
        for img in self.anim_rflame:
            self.transformed_anim_rflame.append(pygame.transform.scale(img, (img.get_width() - 15, img.get_height() - 15)))
        self.anim_index = 0
        self.frame_length_max = 10
        self.frame_length = self.frame_length_max
        self.image = self.transformed_anim_rflame[self.anim_index]
        self.rect = self.image.get_rect()
        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        max_index = len(self.anim_rflame) - 1
        if self.frame_length == 0:
            self.anim_index += 1
            if self.anim_index > max_index:
                self.anim_index = 0
            else:
                self.image = self.transformed_anim_rflame[self.anim_index]
                self.frame_length = self.frame_length_max
        else:
            self.frame_length -= 1


class Target_Engines(pygame.sprite.Sprite):
    def __init__(self):
        super(Target_Engines, self).__init__()
        self.img_explosion_01 = pygame.image.load("bad_engine1.png").convert_alpha()
        self.img_explosion_02 = pygame.image.load("bad_engine2.png").convert_alpha()
        self.img_explosion_03 = pygame.image.load("bad_engine3.png").convert_alpha()
        self.img_explosion_04 = pygame.image.load("bad_engine4.png").convert_alpha()
        self.img_explosion_05 = pygame.image.load("bad_engine5.png").convert_alpha()

        self.anim_tgengine = [self.img_explosion_01,
                               self.img_explosion_02,
                               self.img_explosion_03,
                               self.img_explosion_04,
                               self.img_explosion_05]
        self.anim_index = 0
        self.frame_length_max = 25
        self.frame_length = self.frame_length_max
        self.image = self.anim_tgengine[self.anim_index]
        self.rect = self.image.get_rect()
        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        max_index = len(self.anim_tgengine) - 1
        if self.frame_length == 0:
            self.anim_index += 1
            if self.anim_index > max_index:
                self.anim_index = 0
            else:
                self.image = self.anim_tgengine[self.anim_index]
                self.frame_length = self.frame_length_max
        else:
            self.frame_length -= 1



class Alt_Engines(pygame.sprite.Sprite):
    def __init__(self):
        super(Alt_Engines, self).__init__()
        self.img_explosion_01 = pygame.image.load("bad_engine1.png").convert_alpha()
        self.img_explosion_02 = pygame.image.load("bad_engine2.png").convert_alpha()
        self.img_explosion_03 = pygame.image.load("bad_engine3.png").convert_alpha()
        self.img_explosion_04 = pygame.image.load("bad_engine4.png").convert_alpha()
        self.img_explosion_05 = pygame.image.load("bad_engine5.png").convert_alpha()

        self.anim_tgengine = [self.img_explosion_01,
                              self.img_explosion_02,
                              self.img_explosion_03,
                              self.img_explosion_04,
                              self.img_explosion_05]
        self.anim_index = 0
        self.frame_length_max = 30
        self.frame_length = self.frame_length_max
        self.image = self.anim_tgengine[self.anim_index]
        self.rect = self.image.get_rect()
        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        max_index = len(self.anim_tgengine) - 1
        if self.frame_length == 0:
            self.anim_index += 1
            if self.anim_index > max_index:
                self.anim_index = 0
            else:
                self.image = self.anim_tgengine[self.anim_index]
                self.frame_length = self.frame_length_max
        else:
            self.frame_length -= 1
