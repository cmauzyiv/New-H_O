import pygame
import constance as c

class YAsteroidScore(pygame.sprite.Sprite):
    def __init__(self):
        super(YAsteroidScore, self).__init__()
        self.value = 0
        self.font_size = 25
        self.color = (255, 255, 255)
        self.font = pygame.font.Font(None, self.font_size)
        self.image = self.font.render(str(f'Yellow: {self.value}'), False, self.color, None)
        self.rect = self.image.get_rect()
        self.x_pad = 300
        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        pass

    def update_score(self, value):
        self.value += value
        self.image = self.font.render(str(f'Yellow: {self.value}'), False, self.color, None)
        self.rect = self.image.get_rect()



class BAsteroidScore(pygame.sprite.Sprite):
    def __init__(self):
        super(BAsteroidScore, self).__init__()
        self.value = 0
        self.font_size = 25
        self.color = (255, 255, 255)
        self.font = pygame.font.Font(None, self.font_size)
        self.image = self.font.render(str(f'Blue: {self.value}'), False, self.color, None)
        self.rect = self.image.get_rect()
        self.x_pad = 200
        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        pass

    def update_score(self, value):
        self.value += value
        self.image = self.font.render(str(f'Blue: {self.value}'), False, self.color, None)
        self.rect = self.image.get_rect()

class RAsteroidScore(pygame.sprite.Sprite):
    def __init__(self):
        super(RAsteroidScore, self).__init__()
        self.value = 0
        self.font_size = 25
        self.color = (255, 255, 255)
        self.font = pygame.font.Font(None, self.font_size)
        self.image = self.font.render(str(f'Red: {self.value}'), False, self.color, None)
        self.rect = self.image.get_rect()
        self.x_pad = 100
        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        pass

    def update_score(self, value):
        self.value += value
        self.image = self.font.render(str(f'Red: {self.value}'), False, self.color, None)
        self.rect = self.image.get_rect()
