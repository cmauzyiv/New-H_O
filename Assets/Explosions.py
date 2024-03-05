import pygame

class ShipExplosions(pygame.sprite.Sprite):
    def __init__(self):
        super(ShipExplosions, self).__init__()
        self.img_explosion_01 = pygame.image.load("regularExplosion00.png").convert_alpha()
        self.img_explosion_02 = pygame.image.load("regularExplosion01.png").convert_alpha()
        self.img_explosion_03 = pygame.image.load("regularExplosion02.png").convert_alpha()
        self.img_explosion_04 = pygame.image.load("regularExplosion03.png").convert_alpha()
        self.img_explosion_05 = pygame.image.load("regularExplosion04.png").convert_alpha()
        self.img_explosion_06 = pygame.image.load("regularExplosion05.png").convert_alpha()
        self.img_explosion_07 = pygame.image.load("regularExplosion06.png").convert_alpha()
        self.img_explosion_08 = pygame.image.load("regularExplosion07.png").convert_alpha()
        self.img_explosion_09 = pygame.image.load("regularExplosion08.png").convert_alpha()

        self.anim_explosion = [self.img_explosion_01,
                               self.img_explosion_02,
                               self.img_explosion_03,
                               self.img_explosion_04,
                               self.img_explosion_05,
                               self.img_explosion_06,
                               self.img_explosion_07,
                               self.img_explosion_08,
                               self.img_explosion_09]
        self.anim_index = 0
        self.frame_length_max = 5
        self.frame_length = self.frame_length_max
        self.image = self.anim_explosion[self.anim_index]
        self.rect = self.image.get_rect()
        self.kill_timer = 60
        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        self.image = self.anim_explosion[self.anim_index]
        max_index = len(self.anim_explosion) - 1
        if self.frame_length == 0:
            self.anim_index += 1
            if self.anim_index > max_index:
                self.kill()
            else:
                self.image = self.anim_explosion[self.anim_index]
                self.frame_length = self.frame_length_max
        else:
            self.frame_length -= 1
        if self.kill_timer == 0:
            self.kill()
        else:
            self.kill_timer -= 1


class P1AsteroidExplosions(pygame.sprite.Sprite):
    def __init__(self):
        super(P1AsteroidExplosions, self).__init__()
        self.img_explosion_01 = pygame.image.load("spark_01.png").convert_alpha()
        self.img_explosion_02 = pygame.image.load("spark_02.png").convert_alpha()
        self.img_explosion_03 = pygame.image.load("spark_03.png").convert_alpha()
        self.img_explosion_04 = pygame.image.load("spark_04.png").convert_alpha()
        self.img_explosion_05 = pygame.image.load("spark_05.png").convert_alpha()
        self.img_explosion_06 = pygame.image.load("spark_06.png").convert_alpha()
        self.img_explosion_07 = pygame.image.load("spark_07.png").convert_alpha()
        self.img_explosion_08 = pygame.image.load("spark_08.png").convert_alpha()
        self.img_explosion_09 = pygame.image.load("spark_09.png").convert_alpha()
        self.img_explosion_10 = pygame.image.load("spark_10.png").convert_alpha()

        self.anim_explosion = [self.img_explosion_01,
                               self.img_explosion_02,
                               self.img_explosion_03,
                               self.img_explosion_04,
                               self.img_explosion_05,
                               self.img_explosion_06,
                               self.img_explosion_07,
                               self.img_explosion_08,
                               self.img_explosion_09,
                               self.img_explosion_10
                               ]
        self.anim_index = 0
        self.frame_length_max = 3
        self.frame_length = self.frame_length_max
        self.image = self.anim_explosion[self.anim_index]
        self.rect = self.image.get_rect()
        self.kill_timer = 60
        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        self.image = self.anim_explosion[self.anim_index]
        max_index = len(self.anim_explosion) - 1
        if self.frame_length == 0:
            self.anim_index += 1
            if self.anim_index > max_index:
                self.kill()
            else:
                self.image = self.anim_explosion[self.anim_index]
                self.frame_length = self.frame_length_max
        else:
            self.frame_length -= 1
        if self.kill_timer == 0:
            self.kill()
        else:
            self.kill_timer -= 1



class P2AsteroidExplosions(pygame.sprite.Sprite):
    def __init__(self):
        super(P2AsteroidExplosions, self).__init__()
        self.img_explosion_01 = pygame.image.load("p2astexplosion1.png").convert_alpha()
        self.img_explosion_02 = pygame.image.load("p2astexplosion2.png").convert_alpha()
        self.img_explosion_03 = pygame.image.load("p2astexplosion3.png").convert_alpha()
        self.img_explosion_04 = pygame.image.load("p2astexplosion4.png").convert_alpha()
        self.img_explosion_05 = pygame.image.load("p2astexplosion5.png").convert_alpha()
        self.img_explosion_06 = pygame.image.load("p2astexplosion6.png").convert_alpha()
        self.img_explosion_07 = pygame.image.load("p2astexplosion7.png").convert_alpha()
        self.img_explosion_08 = pygame.image.load("p2astexplosion8.png").convert_alpha()
        self.img_explosion_09 = pygame.image.load("p2astexplosion9.png").convert_alpha()
        self.img_explosion_10 = pygame.image.load("p2astexplosion10.png").convert_alpha()

        self.anim_explosion = [self.img_explosion_01,
                               self.img_explosion_02,
                               self.img_explosion_03,
                               self.img_explosion_04,
                               self.img_explosion_05,
                               self.img_explosion_06,
                               self.img_explosion_07,
                               self.img_explosion_08,
                               self.img_explosion_09,
                               self.img_explosion_10]
        self.anim_index = 0
        self.frame_length_max = 5
        self.frame_length = self.frame_length_max
        self.image = self.anim_explosion[self.anim_index]
        self.rect = self.image.get_rect()
        self.kill_timer = 60
        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        self.image = self.anim_explosion[self.anim_index]
        max_index = len(self.anim_explosion) - 1
        if self.frame_length == 0:
            self.anim_index += 1
            if self.anim_index > max_index:
                self.kill()
            else:
                self.image = self.anim_explosion[self.anim_index]
                self.frame_length = self.frame_length_max
        else:
            self.frame_length -= 1
        if self.kill_timer == 0:
            self.kill()
        else:
            self.kill_timer -= 1

class SdAsteroidExplosions(pygame.sprite.Sprite):
    def __init__(self):
        super(SdAsteroidExplosions, self).__init__()
        self.img_explosion_01 = pygame.image.load("sd_asteroid_explosion1.png").convert_alpha()
        self.img_explosion_02 = pygame.image.load("sd_asteroid_explosion2.png").convert_alpha()
        self.img_explosion_03 = pygame.image.load("sd_asteroid_explosion3.png").convert_alpha()
        self.img_explosion_04 = pygame.image.load("sd_asteroid_explosion4.png").convert_alpha()
        self.img_explosion_05 = pygame.image.load("sd_asteroid_explosion5.png").convert_alpha()
        self.img_explosion_06 = pygame.image.load("sd_asteroid_explosion6.png").convert_alpha()
        self.img_explosion_07 = pygame.image.load("sd_asteroid_explosion7.png").convert_alpha()
        self.img_explosion_08 = pygame.image.load("sd_asteroid_explosion8.png").convert_alpha()
        self.img_explosion_09 = pygame.image.load("sd_asteroid_explosion9.png").convert_alpha()
        self.img_explosion_10 = pygame.image.load("sd_asteroid_explosion10.png").convert_alpha()
        self.anim_explosion = [self.img_explosion_01,
                               self.img_explosion_02,
                               self.img_explosion_03,
                               self.img_explosion_04,
                               self.img_explosion_05,
                               self.img_explosion_06,
                               self.img_explosion_07,
                               self.img_explosion_08,
                               self.img_explosion_09,
                               self.img_explosion_10]
        self.anim_index = 0
        self.frame_length_max = 5
        self.frame_length = self.frame_length_max
        self.image = self.anim_explosion[self.anim_index]
        self.rect = self.image.get_rect()
        self.kill_timer = 60
        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        self.image = self.anim_explosion[self.anim_index]
        max_index = len(self.anim_explosion) - 1
        if self.frame_length == 0:
            self.anim_index += 1
            if self.anim_index > max_index:
                self.kill()
            else:
                self.image = self.anim_explosion[self.anim_index]
                self.frame_length = self.frame_length_max
        else:
            self.frame_length -= 1
        if self.kill_timer == 0:
            self.kill()
        else:
            self.kill_timer -= 1

class SdeltaAsteroidExplosions(pygame.sprite.Sprite):
    def __init__(self):
        super(SdeltaAsteroidExplosions, self).__init__()
        self.img_explosion_01 = pygame.image.load("sdelta_explosion1.png").convert_alpha()
        self.img_explosion_02 = pygame.image.load("sdelta_explosion2.png").convert_alpha()
        self.img_explosion_03 = pygame.image.load("sdelta_explosion3.png").convert_alpha()
        self.img_explosion_04 = pygame.image.load("sdelta_explosion4.png").convert_alpha()
        self.img_explosion_05 = pygame.image.load("sdelta_explosion5.png").convert_alpha()
        self.img_explosion_06 = pygame.image.load("sdelta_explosion6.png").convert_alpha()
        self.img_explosion_07 = pygame.image.load("sdelta_explosion7.png").convert_alpha()
        self.img_explosion_08 = pygame.image.load("sdelta_explosion8.png").convert_alpha()
        self.img_explosion_09 = pygame.image.load("sdelta_explosion9.png").convert_alpha()
        self.img_explosion_10 = pygame.image.load("sdelta_explosion10.png").convert_alpha()
        self.anim_explosion = [self.img_explosion_01,
                               self.img_explosion_02,
                               self.img_explosion_03,
                               self.img_explosion_04,
                               self.img_explosion_05,
                               self.img_explosion_06,
                               self.img_explosion_07,
                               self.img_explosion_08,
                               self.img_explosion_09,
                               self.img_explosion_10]
        self.anim_index = 0
        self.frame_length_max = 3
        self.frame_length = self.frame_length_max
        self.image = self.anim_explosion[self.anim_index]
        self.rect = self.image.get_rect()
        self.kill_timer = 60
        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        self.image = self.anim_explosion[self.anim_index]
        max_index = len(self.anim_explosion) - 1
        if self.frame_length == 0:
            self.anim_index += 1
            if self.anim_index > max_index:
                self.kill()
            else:
                self.image = self.anim_explosion[self.anim_index]
                self.frame_length = self.frame_length_max
        else:
            self.frame_length -= 1
        if self.kill_timer == 0:
            self.kill()
        else:
            self.kill_timer -= 1