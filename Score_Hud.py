import pygame
import constance as c
from Score import Score, Level
##from Asteroid_Score import AsteroidScore


class Score_HUD(pygame.sprite.Sprite):
    def __init__(self):
        super(Score_HUD, self).__init__()
        self.image = pygame.image.load("hud3.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = (c.middle_wall - 115)
        self.rect.y = c.display_height - 60
        self.image = pygame.transform.scale(self.image, ((self.image.get_width() //2) + 35, self.image.get_height() // 2))
        self.vel_x = 0
        self.vel_y = 0
        self.score = Score()
        self.score_group = pygame.sprite.Group()
        self.score_group.add(self.score)
        self.level = Level()
        self.level_group = pygame.sprite.Group()
        self.level_group.add(self.level)
        self.score.rect.x = self.rect.x + 65
        self.score.rect.y = self.rect.y + 75
        self.level.rect.x = self.rect.x - 150
        self.level.rect.y = self.rect.y + 10
        ##self.asteroid_score = AsteroidScore()
        ##self.asteroid_score_group = pygame.sprite.Group()
        ##self.asteroid_score_group.add(self.asteroid_score)

    def update(self):
        self.score_group.update()
        self.level_group.update()
        for level in self.level_group:
            level.rect.x = self.rect.x - 150
            level.rect.y = self.rect.y + 10
        ##self.asteroid_score_group.update()
        if self.score.value <= 9:
            self.score.rect.x = self.rect.x + 50
            self.score.rect.y = self.rect.y + 9
        elif self.score.value <= 99:
            self.score.rect.x = self.rect.x + 40
            self.score.rect.y = self.rect.y + 9
        elif self.score.value <= 999:
            self.score.rect.x = self.rect.x + 35
            self.score.rect.y = self.rect.y + 9
        elif self.score.value <= 9999:
            self.score.rect.x = self.rect.x + 30
            self.score.rect.y = self.rect.y + 9
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
