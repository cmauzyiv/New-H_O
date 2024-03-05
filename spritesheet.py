import pygame


class SpriteSheet:
    def __init__(self, filename):
        self.sprite_sheet = pygame.image.load("enemy_fighter_3_ani_strip22.png.png").convert_alpha()

    def get_image(self, x, y, width, height):
        return self.sprite_sheet.subsurface((x, y, width, height))

class Shipbad3(pygame.sprite.Sprite): ##this is how the ship will look and spawn
    def __init__(self):
        super(Shipbad3, self).__init__()
        self.vel_x = 0
        self.vel_y = 0
        self.sprite_sheet = pygame.image.load("enemy_fighter_3_ani_strip22.png").convert_alpha()
        self.image = self.get_image(1122, 0, 101, 126)
        self.rect = self.image.get_rect()
        self.anim_img_01 = self.get_image(0,0,  101, 126)
        self.anim_img_02 = self.get_image(102, 0, 101, 126)
        self.anim_index = 0
        self.frame_length_max = 5
        self.turn_index = 0
        self.frame_length = self.frame_length_max




    def get_image(self, x, y, width, height):
        return self.sprite_sheet.subsurface((x, y, width, height))

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y