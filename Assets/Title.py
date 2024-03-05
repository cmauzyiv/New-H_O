import pygame
from start_game import StartGame
import constance as c


class StartMenu(pygame.sprite.Sprite):
    def __init__(self):
        super(StartMenu, self).__init__()
        self.image = pygame.Surface(c.display_size)
        self.color = (255, 255, 255)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.size = (self.width, self.height)
        self.image = pygame.Surface(self.size)
        self.color = (255, 255, 255)
        self.image.fill(self.color)
        self.start = pygame.sprite.Group()



    def update(self):
        self.start.update()
        new_start = StartGame()
        self.start.add(new_start)
        self.start.draw(self.image)




##def draw_start_menu():
  ##  display.fill((0,0,0))
    ##font = pygame.font.SysFont('arial', 40)
    ##title = font.render('Press Enter', True, (255, 255, 255))
    ##display.blit(title, (c.display_width // 2 - title.get_width() // 2, c.display_height // 2 - title.get_height() //2))
