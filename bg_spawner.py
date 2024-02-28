import pygame
import constance as c
from new_background import NewBg, p2NewBg, p3NewBg, p4NewBg
from star import Star
from badguy1 import Shipbad1
from badguy2 import ShipBad2
from asteroid import Asteroid
import random



class P1BgSpawner: ##this is when it will spawn
    def __init__(self):
        self.bg_group = pygame.sprite.Group()
        self.bg_list = []
        self.num_bg = 0
        self.stars_group = pygame.sprite.Group()
        self.num_stars = 0



    def update(self):
        self.bg_group.update()
        if self.num_bg == 0:
            new_bg = NewBg()
            self.bg_group.add(new_bg)
            self.num_bg += 1
        for new_bg in self.bg_group:
            if self.num_bg == 1:
                if new_bg.rect.y == -800:
                    new_bg = NewBg()
                    self.bg_group.add(new_bg)
                    new_bg.rect.y = c.display_height
                    self.num_bg += 1
            if new_bg.rect.y == -1600:
                self.bg_group.remove(new_bg)
                self.num_bg -= 1
        self.stars_group.update()
        if self.num_stars == 0:
            new_stars = Star()
            self.stars_group.add(new_stars)
            self.num_stars += 1
        for new_stars in self.stars_group:
            if self.num_stars == 1:
                if new_stars.rect.y == -800:
                    new_stars = Star()
                    self.stars_group.add(new_stars)
                    new_stars.rect.y = c.display_height
                    self.num_stars += 1
            if new_stars.rect.y == -1600:
                self.stars_group.remove(new_stars)
                self.num_stars -= 1


class P2BgSpawner: ##this is when it will spawn
    def __init__(self):
        self.bg_group = pygame.sprite.Group()
        self.stars_group = pygame.sprite.Group()
        self.bg_list = []
        self.num_bg = 0
        self.num_stars = 0


    def update(self):
        self.bg_group.update()
        if self.num_bg == 0:
            new_bg = p2NewBg()
            self.bg_group.add(new_bg)
            self.num_bg += 1
        for new_bg in self.bg_group:
            if self.num_bg == 1:
                if new_bg.rect.y == -800:
                    new_bg = p2NewBg()
                    self.bg_group.add(new_bg)
                    new_bg.rect.y = c.display_height
                    self.num_bg += 1
            if new_bg.rect.y == -1600:
                self.bg_group.remove(new_bg)
                self.num_bg -= 1
        self.stars_group.update()
        if self.num_stars == 0:
            new_stars = Star()
            self.stars_group.add(new_stars)
            self.num_stars += 1
        for new_stars in self.stars_group:
            if self.num_stars == 1:
                if new_stars.rect.y == -800:
                    new_stars = Star()
                    self.stars_group.add(new_stars)
                    new_stars.rect.y = c.display_height
                    self.num_stars += 1
            if new_stars.rect.y == -1600:
                self.stars_group.remove(new_stars)
                self.num_stars -= 1
class P3BgSpawner: ##this is when it will spawn
    def __init__(self):
        self.bg_group = pygame.sprite.Group()
        self.stars_group = pygame.sprite.Group()
        self.bg_list = []
        self.num_bg = 0
        self.num_stars = 0


    def update(self):
        self.bg_group.update()
        if self.num_bg == 0:
            new_bg = p3NewBg()
            self.bg_group.add(new_bg)
            self.num_bg += 1
        for new_bg in self.bg_group:
            if self.num_bg == 1:
                if new_bg.rect.y == -800:
                    new_bg = p3NewBg()
                    self.bg_group.add(new_bg)
                    new_bg.rect.y = c.display_height
                    self.num_bg += 1
            if new_bg.rect.y == -1600:
                self.bg_group.remove(new_bg)
                self.num_bg -= 1
        self.stars_group.update()
        if self.num_stars == 0:
            new_stars = Star()
            self.stars_group.add(new_stars)
            self.num_stars += 1
        for new_stars in self.stars_group:
            if self.num_stars == 1:
                if new_stars.rect.y == -400:
                    new_stars = Star()
                    self.stars_group.add(new_stars)
                    new_stars.rect.y = c.display_height
                    self.num_stars += 1
            if new_stars.rect.y == -1200:
                self.stars_group.remove(new_stars)
                self.num_stars -= 1

class P4BgSpawner: ##this is when it will spawn
    def __init__(self):
        self.bg_group = pygame.sprite.Group()
        self.stars_group = pygame.sprite.Group()
        self.bg_list = []
        self.num_bg = 0
        self.stars_group = pygame.sprite.Group()
        self.num_stars = 0


    def update(self):
        self.bg_group.update()
        if self.num_bg == 0:
            new_bg = p4NewBg()
            self.bg_group.add(new_bg)
            self.num_bg += 1
        for new_bg in self.bg_group:
            if self.num_bg == 1:
                if new_bg.rect.y == -800:
                    new_bg = p4NewBg()
                    self.bg_group.add(new_bg)
                    new_bg.rect.y = c.display_height
                    self.num_bg += 1
            if new_bg.rect.y == -1600:
                self.bg_group.remove(new_bg)
                self.num_bg -= 1
        self.stars_group.update()
        if self.num_stars == 0:
            new_stars = Star()
            self.stars_group.add(new_stars)
            self.num_stars += 1
        for new_stars in self.stars_group:
            if self.num_stars == 1:
                if new_stars.rect.y == -400:
                    new_stars = Star()
                    self.stars_group.add(new_stars)
                    new_stars.rect.y = c.display_height
                    self.num_stars += 1
            if new_stars.rect.y == -1200:
                self.stars_group.remove(new_stars)
                self.num_stars -= 1
