import pygame
import constance as c
from particle_spawner import ParticleSpawner
import random
from spritesheet1 import SpriteSheet

class SdAsteroid(pygame.sprite.Sprite): ##this is how the ship will look and spawn
    def __init__(self):
        super(SdAsteroid, self).__init__()
        self.img_explosion_01 = pygame.image.load("sd_asteroid_explosion1.png").convert_alpha()
        self.img_explosion_02 = pygame.image.load("sd_asteroid_explosion2.png").convert_alpha()
        self.img_explosion_03 = pygame.image.load("sd_asteroid_explosion3.png").convert_alpha()
        self.img_explosion_04 = pygame.image.load("sd_asteroid_explosion4.png").convert_alpha()
        self.img_explosion_05 = pygame.image.load("sd_asteroid_explosion5.png").convert_alpha()
        self.img_explosion_06 = pygame.image.load("sd_asteroid_explosion6.png").convert_alpha()
        self.anim_explosion = [self.img_explosion_01,
                               self.img_explosion_02,
                               self.img_explosion_03,
                               self.img_explosion_04,
                               self.img_explosion_05,
                               self.img_explosion_06]

        self.anim_index = 0
        self.frame_length_max = 7
        self.frame_length = self.frame_length_max
        self.image = pygame.image.load("sd_asteroid1.png").convert_alpha()
        self.scale_value = random.uniform(1, 1.5)
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * self.scale_value),
                                            int(self.image.get_height()* self.scale_value)))
        self.rect = self.image.get_rect()
        self.is_destroyed = False
        self.is_invincible = False
        self.rect.x = random.randrange(0, (c.display_width - self.rect.width))
        self.rect.y = -self.rect.height
        self.hp_timer = random.randrange(60, 1000)
        self.hp = 0 ##this is how i will probably do reinforcement schedule. I set HP or IRT then down below, i will make it so that it will only blow up after meets irt
        self.point_value = 1
        self.lasers = pygame.sprite.Group()
        self.snd_hit = pygame.mixer.Sound("tie_explosion.ogg")
        self.vel_x = 0
        self.vel_y = 1 #how fast its moving down y axis
        self.speed = 5

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        if self.is_destroyed:
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





    def get_hit(self):
        if not self.is_invincible:
            self.snd_hit.play()
            self.is_destroyed = True
            self.rect.x = self.rect.x - 30
            self.rect.y = self.rect.y - 30
            self.image = self.anim_explosion[self.anim_index]
        else:
            self.snd_hit.play()
