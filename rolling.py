import pygame


class Roll_Effect(pygame.sprite.Sprite): ##this is how the ship will look and spawn
    def __init__(self):
        super(Roll_Effect, self).__init__()
        self.main_image = pygame.image.load("roll_effect.png").convert_alpha()
        self.rect = self.main_image.get_rect()
        self.main_image_center = self.main_image.get_rect().center
        self.img_effect_01 = pygame.transform.rotate(self.main_image, 60)
        self.img_effect_02 = pygame.transform.rotate(self.main_image, 120)
        self.img_effect_03 = pygame.transform.rotate(self.main_image, 200)
        self.img_effect_04 = pygame.transform.rotate(self.main_image, 240)
        self.img_effect_05 = pygame.transform.rotate(self.main_image, 300)

        self.anim_roll_effect = [self.img_effect_01, self.img_effect_02,
                                 self.img_effect_04, self.img_effect_05]
        self.anim_index = 0
        self.frame_length_max = 15
        self.frame_length = self.frame_length_max
        self.image = self.anim_roll_effect[self.anim_index]
        self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        
        max_index = len(self.anim_roll_effect) - 1
        if self.frame_length == 0:
            self.anim_index += 1
            if self.anim_index > max_index:
                self.kill()
            else:
                self.image = self.anim_roll_effect[self.anim_index]
                self.rect = self.image.get_rect(midbottom=self.rect.midbottom)
                self.frame_length = self.frame_length_max
        else:
            self.frame_length -= 1