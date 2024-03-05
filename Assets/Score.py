import pygame
import constance as c

class Score(pygame.sprite.Sprite):
    def __init__(self):
        super(Score, self).__init__()
        self.value = 0
        self.font_size = 40
        self.color = (255, 255, 255)
        self.font = pygame.font.Font(None, self.font_size)
        self.image = self.font.render(str(f'Points: {self.value}'), False, self.color, None)
        self.rect = self.image.get_rect()
        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        pass

    def update_score(self, value):
        self.value += value
        self.image = self.font.render(str(f'Points: {self.value}'), False, self.color, None)
        self.rect = self.image.get_rect()
        self.rect.x = self.vel_x
        self.rect.y = self.vel_y

class Level(pygame.sprite.Sprite):
    def __init__(self):
        super(Level, self).__init__()
        self.value = 1
        self.font_size = 40
        self.color = (255, 255, 255)
        self.font = pygame.font.Font(None, self.font_size)
        self.image = self.font.render(str(f'Level: {self.value}'), False, self.color, None)
        self.rect = self.image.get_rect()
        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        self.image = self.font.render(str(f'Level: {self.value}'), False, self.color, None)
        self.rect = self.image.get_rect()
        self.rect.x = self.vel_x
        self.rect.y = self.vel_y

    def update_level(self, value):
        self.value += value
        self.image = self.font.render(str(f'Level: {self.value}'), False, self.color, None)
        self.rect = self.image.get_rect()
        self.rect.x = self.vel_x
        self.rect.y = self.vel_y