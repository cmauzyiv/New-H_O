import pygame



class Spinning(pygame.sprite.Sprite):
    def __init__(self):
        super(Spinning, self).__init__()
        self.img_spin_01 = pygame.image.load("spin_01.png").convert_alpha()
        self.img_spin_02 = pygame.image.load("spin_02.png").convert_alpha()
        self.img_spin_03 = pygame.image.load("spin_03.png").convert_alpha()
        self.img_spin_04 = pygame.image.load("spin_04.png").convert_alpha()
        self.img_spin_05 = pygame.image.load("spin_05.png").convert_alpha()
        self.img_spin_06 = pygame.image.load("spin_06.png").convert_alpha()
        self.img_spin_07 = pygame.image.load("spin_07.png").convert_alpha()
        self.img_spin_08 = pygame.image.load("spin_08.png").convert_alpha()
        self.img_spin_09 = pygame.image.load("spin_09.png").convert_alpha()
        self.img_spin_10 = pygame.image.load("spin_10.png").convert_alpha()

        self.anim_spin = [self.img_spin_01, self.img_spin_02, self.img_spin_03,
                          self.img_spin_04, self.img_spin_05, self.img_spin_06,
                          self.img_spin_07, self.img_spin_08, self.img_spin_09,
                          self.img_spin_10]

        self.anim_index = 0
        self.frame_length_max = 7
        self.frame_length = self.frame_length_max
        self.image = self.anim_spin[self.anim_index]
        self.rect = self.image.get_rect()
        self.vel_x = 0
        self.vel_y = 0


    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        max_index = len(self.anim_spin) - 1
        if self.frame_length == 0:
            self.anim_index += 1
            if self.anim_index > max_index:
                self.kill()
            else:
                self.image = self.anim_spin[self.anim_index]
                self.frame_length = self.frame_length_max
        else:
            self.frame_length -= 1

