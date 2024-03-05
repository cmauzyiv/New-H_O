import pygame
import spritesheet
import time
from spritesheet import SpriteSheet

class ShipShield1(pygame.sprite.Sprite):
    def __init__(self):
        super(ShipShield1, self).__init__()
        self.sheet_image = pygame.image.load("shield_loop.png").convert_alpha()
        self.sprite_sheet = spritesheet.SpriteSheet(self.sheet_image)
        self.frame_0 = self.sprite_sheet.get_image(0, 128, 128, 3, (0,0,0))
        self.frame_1 = self.sprite_sheet.get_image(1, 128, 128, 3, (0, 0, 0))
        self.frame_2 = self.sprite_sheet.get_image(2, 128, 128, 3, (0, 0, 0))
        self.frame_3 = self.sprite_sheet.get_image(3, 128, 128, 3, (0, 0, 0))
        self.frame_4 = self.sprite_sheet.get_image(4, 128, 128, 3, (0, 0, 0))
        self.frame_5 = self.sprite_sheet.get_image(5, 128, 128, 3, (0, 0, 0))
        self.frame_6 = self.sprite_sheet.get_image(6, 128, 128, 3, (0, 0, 0))
        self.frame_7 = self.sprite_sheet.get_image(7, 128, 128, 3, (0, 0, 0))
        self.frame_8 = self.sprite_sheet.get_image(8, 128, 128, 3, (0, 0, 0))
        self.frame_9 = self.sprite_sheet.get_image(9, 128, 128, 3, (0, 0, 0))
        self.frame_10 = self.sprite_sheet.get_image(10, 128, 128, 3, (0, 0, 0))
        self.frame_11 = self.sprite_sheet.get_image(11, 128, 128, 3, (0, 0, 0))
        self.rect = self.sheet_image.get_rect()
        self.animation_cooldown = 300
        self.animation_list = []
        self.animation_steps = 11
        self.frame = 0
        for x in range(self.animation_steps):
            self.animation_list.append(self.sprite_sheet.get_image(x, 128, 128, 3, (0, 0, 0)))
        ##self.current_frame = (self.current_frame + 1) % len(self.frames)
        self.kill_timer = 60
        self.vel_x = 0
        self.vel_y = 0
        self.last_update = pygame.time.get_ticks()
        self.image = self.animation_list[self.frame], (0, 0)

    def update(self):
        self.image = self.animation_list[self.frame], (0, 0)
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.animation_cooldown:
            self.frame += 1
            self.last_update = current_time




