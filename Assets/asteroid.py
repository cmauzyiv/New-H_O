import pygame
import constance as c
from particle_spawner import ParticleSpawner
import random
from Explosions import P1AsteroidExplosions

class Asteroid(pygame.sprite.Sprite): ##this is how the ship will look and spawn
    def __init__(self):
        super(Asteroid, self).__init__()
        self.anim_index = 0
        self.frame_length_max = 7
        self.frame_length = self.frame_length_max
        self.img_asteroid_01 = pygame.image.load('gem1_01.png').convert_alpha()
        self.img_asteroid_02 = pygame.image.load('gem1_02.png').convert_alpha()
        self.img_asteroid_03 = pygame.image.load('gem1_03.png').convert_alpha()
        self.img_asteroid_04 = pygame.image.load('gem1_04.png').convert_alpha()
        self.img_asteroid_05 = pygame.image.load('gem1_05.png').convert_alpha()
        self.img_asteroid_06 = pygame.image.load('gem1_06.png').convert_alpha()
        self.img_asteroid_07 = pygame.image.load('gem1_07.png').convert_alpha()
        self.img_asteroid_08 = pygame.image.load('gem1_08.png').convert_alpha()
        self.img_asteroid_09 = pygame.image.load('gem1_09.png').convert_alpha()
        self.img_asteroid_10 = pygame.image.load('gem1_10.png').convert_alpha()
        self.img_asteroid_11 = pygame.image.load('gem1_11.png').convert_alpha()

        self.anim_asteroid = [self.img_asteroid_01, self.img_asteroid_02, self.img_asteroid_03,
                              self.img_asteroid_04, self.img_asteroid_05, self.img_asteroid_06,
                              self.img_asteroid_07, self.img_asteroid_08, self.img_asteroid_09,
                              self.img_asteroid_10, self.img_asteroid_11]

        self.image = self.anim_asteroid[self.anim_index]
        self.scale_value = random.uniform(.5, 1)
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * self.scale_value),
                                            int(self.image.get_height()* self.scale_value)))
        self.rect = self.image.get_rect()
        self.explosion_group = pygame.sprite.Group()
        self.is_destroyed = False
        self.is_invincible = False
        self.rect.x = random.randrange(0, (c.display_width - self.rect.width))
        self.rect.y = -self.rect.height
        self.hp_timer = random.randrange(60, 1000)
        self.hp = 0 ##this is how i will probably do reinforcement schedule. I set HP or IRT then down below, i will make it so that it will only blow up after meets irt
        self.point_value = 1
        self.lasers = pygame.sprite.Group()
        ##self.snd_hit = pygame.mixer.Sound("asteroid_sound.ogg")
        self.vel_x = 0
        self.vel_y = 1 #how fast its moving down y axis
        self.speed = 5

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        self.explosion_group.update()
        max_index = len(self.anim_asteroid) - 1
        if self.frame_length == 0:
            self.anim_index += 1
            if self.anim_index > max_index:
                self.anim_index = 0
            else:
                self.image = self.anim_asteroid[self.anim_index]
                self.frame_length = self.frame_length_max
        else:
            self.frame_length -= 1




    def get_hit(self):
        if not self.is_invincible:
            ##self.snd_hit.play()
            self.is_destroyed = True
            new_explosion = P1AsteroidExplosions()
            new_explosion.rect.x = self.rect.x + 16
            new_explosion.rect.y = self.rect.y
            self.explosion_group.add(new_explosion)
            self.rect.x = self.rect.x
            self.rect.y = self.rect.y 
            self.image = new_explosion.anim_explosion[new_explosion.anim_index]
        else:
            self.snd_hit.play()


