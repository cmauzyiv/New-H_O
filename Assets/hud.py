import pygame
import constance as c
from Score import Score
from lives import Lives




class HUD(pygame.sprite.Sprite):
    def __init__(self, num_lives):
        super(HUD, self).__init__()
        self.image = pygame.image.load("hud3.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = ((c.display_width // 3) - 65)
        self.rect.y = c.display_height - 50
        self.image = pygame.transform.scale(self.image, ((self.image.get_width() //2) + 35, self.image.get_height() // 2))
        self.vel_x = 0
        self.vel_y = 0
        self.score = Score()
        self.score_group = pygame.sprite.Group()
        self.score_group.add(self.score)
        self.lives = Lives(num_lives)
        self.lives.rect.x = 300
        self.lives.rect.y = c.display_height - 50
        self.icons_group = pygame.sprite.Group()
        self.icons_group.add(self.lives)




    def update(self):
        self.score_group.update()
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

