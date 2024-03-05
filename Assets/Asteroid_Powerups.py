import pygame
import random
import constance as c


class Yellow_Icon(pygame.sprite.Sprite): ##this is how the ship will look and spawn
    def __init__(self):
        super(Yellow_Icon, self).__init__()
        self.img_01 = pygame.image.load("yellow_01.png").convert_alpha()
        self.img_02 = pygame.image.load("yellow_02.png").convert_alpha()
        self.img_03 = pygame.image.load("yellow_03.png").convert_alpha()
        self.img_04 = pygame.image.load("yellow_04.png").convert_alpha()
        self.img_05 = pygame.image.load("yellow_05.png").convert_alpha()
        self.img_06 = pygame.image.load("yellow_06.png").convert_alpha()
        self.img_07 = pygame.image.load("yellow_07.png").convert_alpha()
        self.img_08 = pygame.image.load("yellow_08.png").convert_alpha()
        self.img_09 = pygame.image.load("yellow_09.png").convert_alpha()
        self.img_010 = pygame.image.load("yellow_10.png").convert_alpha()
        self.img_011 = pygame.image.load("yellow_11.png").convert_alpha()
        self.img_012 = pygame.image.load("yellow_12.png").convert_alpha()
        self.img_013 = pygame.image.load("yellow_13.png").convert_alpha()
        self.img_014 = pygame.image.load("yellow_14.png").convert_alpha()

        self.anim_yellow = [self.img_01, self.img_02, self.img_03, self.img_04,
                            self.img_05, self.img_06, self.img_07, self.img_08,
                            self.img_09, self.img_010, self.img_011, self.img_012,
                            self.img_013, self.img_014]
        self.anim_index = 0
        self.frame_length_max = 10
        self.frame_length = self.frame_length_max
        self.image = self.anim_yellow[self.anim_index]
        self.rect = self.image.get_rect()
        self.vel_y = 2
        self.vel_x = 0
        self.rect.x = random.randrange(0, (c.display_width - self.rect.width))
        self.rect.y = -self.rect.height


    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        max_index = len(self.anim_yellow) - 1
        if self.frame_length == 0:
            self.anim_index += 1
            if self.anim_index > max_index:
                self.anim_index = 0
            else:
                self.image = self.anim_yellow[self.anim_index]
                self.frame_length = self.frame_length_max
        else:
            self.frame_length -= 1

class Blue_Icon(pygame.sprite.Sprite): ##this is how the ship will look and spawn
    def __init__(self):
        super(Blue_Icon, self).__init__()
        self.img_01 = pygame.image.load("blue_01.png").convert_alpha()
        self.img_02 = pygame.image.load("blue_02.png").convert_alpha()
        self.img_03 = pygame.image.load("blue_03.png").convert_alpha()
        self.img_04 = pygame.image.load("blue_04.png").convert_alpha()
        self.img_05 = pygame.image.load("blue_05.png").convert_alpha()
        self.img_06 = pygame.image.load("blue_06.png").convert_alpha()
        self.img_07 = pygame.image.load("blue_07.png").convert_alpha()
        self.img_08 = pygame.image.load("blue_08.png").convert_alpha()
        self.img_09 = pygame.image.load("blue_09.png").convert_alpha()
        self.img_010 = pygame.image.load("blue_10.png").convert_alpha()
        self.img_011 = pygame.image.load("blue_11.png").convert_alpha()
        self.img_012 = pygame.image.load("blue_12.png").convert_alpha()
        self.img_013 = pygame.image.load("blue_13.png").convert_alpha()
        self.img_014 = pygame.image.load("blue_14.png").convert_alpha()

        self.anim_blue = [self.img_01, self.img_02, self.img_03, self.img_04,
                            self.img_05, self.img_06, self.img_07, self.img_08,
                            self.img_09, self.img_010, self.img_011, self.img_012,
                            self.img_013, self.img_014]
        self.anim_index = 0
        self.frame_length_max = 10
        self.frame_length = self.frame_length_max
        self.image = self.anim_blue[self.anim_index]
        self.rect = self.image.get_rect()
        self.vel_y = 2
        self.vel_x = 0
        self.rect.x = random.randrange(0, (c.display_width - self.rect.width))
        self.rect.y = -self.rect.height


    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        max_index = len(self.anim_blue) - 1
        if self.frame_length == 0:
            self.anim_index += 1
            if self.anim_index > max_index:
                self.anim_index = 0
            else:
                self.image = self.anim_blue[self.anim_index]
                self.frame_length = self.frame_length_max
        else:
            self.frame_length -= 1

class Red_Icon(pygame.sprite.Sprite): ##this is how the ship will look and spawn
    def __init__(self):
        super(Red_Icon, self).__init__()
        self.img_01 = pygame.image.load("red_01.png").convert_alpha()
        self.img_02 = pygame.image.load("red_02.png").convert_alpha()
        self.img_03 = pygame.image.load("red_03.png").convert_alpha()
        self.img_04 = pygame.image.load("red_04.png").convert_alpha()
        self.img_05 = pygame.image.load("red_05.png").convert_alpha()
        self.img_06 = pygame.image.load("red_06.png").convert_alpha()
        self.img_07 = pygame.image.load("red_07.png").convert_alpha()
        self.img_08 = pygame.image.load("red_08.png").convert_alpha()
        self.img_09 = pygame.image.load("red_09.png").convert_alpha()
        self.img_010 = pygame.image.load("red_10.png").convert_alpha()
        self.img_011 = pygame.image.load("red_11.png").convert_alpha()
        self.img_012 = pygame.image.load("red_12.png").convert_alpha()
        self.img_013 = pygame.image.load("red_13.png").convert_alpha()
        self.img_014 = pygame.image.load("red_14.png").convert_alpha()

        self.anim_red = [self.img_01, self.img_02, self.img_03, self.img_04,
                            self.img_05, self.img_06, self.img_07, self.img_08,
                            self.img_09, self.img_010, self.img_011, self.img_012,
                            self.img_013, self.img_014]
        self.anim_index = 0
        self.frame_length_max = 10
        self.frame_length = self.frame_length_max
        self.image = self.anim_red[self.anim_index]
        self.rect = self.image.get_rect()
        self.vel_y = 2
        self.vel_x = 0
        self.rect.x = random.randrange(0, (c.display_width - self.rect.width))
        self.rect.y = -self.rect.height


    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        max_index = len(self.anim_red) - 1
        if self.frame_length == 0:
            self.anim_index += 1
            if self.anim_index > max_index:
                self.anim_index = 0
            else:
                self.image = self.anim_red[self.anim_index]
                self.frame_length = self.frame_length_max
        else:
            self.frame_length -= 1