import pygame
import constance as c
from new_background import NewBg
from badguy1 import Shipbad1
from badguy2 import ShipBad2
from asteroid import Asteroid
import random



class BgSpawner: ##this is when it will spawn
    def __init__(self):
        self.bg_group = pygame.sprite.Group()
        self.bg_list = []
        self.num_bg = 0


    def update(self):
        self.bg_group.update()
        if self.num_bg == 0:
            new_bg = NewBg()
            self.bg_group.add(new_bg)
            self.num_bg += 1
        for new_bg in self.bg_group:
            if self.num_bg == 1:
                if new_bg.rect.y == -200:
                    new_bg = NewBg()
                    self.bg_group.add(new_bg)
                    new_bg.rect.y = 600
                    self.num_bg += 1
            if new_bg.rect.y == -800:
                self.bg_group.remove(new_bg)
                self.num_bg -= 1


