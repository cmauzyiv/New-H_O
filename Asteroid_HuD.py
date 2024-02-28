import pygame
import constance as c
from Asteroid_Score import YAsteroidScore, BAsteroidScore, RAsteroidScore


class Asteroid_HUD(pygame.sprite.Sprite):
    def __init__(self):
        super(Asteroid_HUD, self).__init__()
        self.image = pygame.image.load("hud1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,
                                            ((self.image.get_width() // 3), self.image.get_height() // 3))
        self.rect = self.image.get_rect()
        self.yscore_group = pygame.sprite.Group()
        self.bscore_group = pygame.sprite.Group()
        self.rscore_group = pygame.sprite.Group()
        self.rect.x = ((c.display_width // 3) + 50)
        self.rect.y += 20
        self.vel_x = 0
        self.vel_y = 0
        self.yscore = YAsteroidScore()
        self.yscore_group.add(self.yscore)
        self.bscore = BAsteroidScore()
        self.bscore_group.add(self.bscore)
        self.rscore = RAsteroidScore()
        self.rscore_group.add(self.rscore)


    def update(self):
        self.yscore_group.update()
        self.rscore_group.update()
        self.bscore_group.update()
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        self.yscore.rect.x = self.rect.x + 25
        self.yscore.rect.y = self.rect.y + 5
        self.bscore.rect.x = self.rect.x + 150
        self.bscore.rect.y = self.rect.y + 5
        self.rscore.rect.x = self.rect.x + 275
        self.rscore.rect.y = self.rect.y + 5

