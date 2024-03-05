import pygame
import constance as c
from particle import Particle
from particle_spawner import ParticleSpawner
import random





class ShipBad2(pygame.sprite.Sprite): ##this is how the ship will look and spawn
    def __init__(self):
        super(ShipBad2, self).__init__()
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
        self.particle_group = pygame.sprite.Group()
        self.image = pygame.image.load("kb1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() - 10, self.image.get_height() - 10 ))
        self.rect = self.image.get_rect()
        self.is_destroyed = False
        self.is_invincible = True
        ##if i wanted to have him randomly appear somewhere (basically for when i have it respawn)
        self.rect.x = random.randrange(0, c.display_width - self.rect.width)
        self.rect.y = random.randrange(0, c.display_height - self.rect.height * 3)
        self.hp = 1 ##this is how i will probably do reinforcement schedule. I set HP or IRT then down below, i will make it so that it will only blow up after meets irt
        self.lasers = pygame.sprite.Group()
        self.laser_timer_max = 60
        self.laser_timer = self.laser_timer_max
        self.point_value = 5
        self.snd_hit = pygame.mixer.Sound("tie_explosion.ogg")
        self.vel_x = 0
        self.vel_y = 0 #how fast its moving down y axis
        self.speed = 5

    def update(self):
        self.lasers.update()
        self.particle_group.update()
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


    def state_fly_down(self):
        if self.init_state:
            self.init_state = False
       ## if self.rect.y >= 200:
         ##   self.state = self.states['READY_TO_DIE']
           ## self.init_state = True

    ##def state_ready_to_die(self):
       ## if self.init_state:
         ##   self.vel_y = 0
           # while self.vel_x == 0:
            #    self.vel_x = random.randrange(-4, 4)
            #self.init_state = False
        #if self.laser_timer == 0:
         #   self.shoot()
          #  self.laser_timer = self.laser_timer_max
       # else:
        #    self.laser_timer -= 1
       # if self.rect.x <= 0:
        #    self.vel_x *= -1
        #elif self.rect.x + self.rect.width >= c.display_width:
         #   self.vel_x *= -1


    def shoot(self):
        new_laser = Laser()
        new_laser.vel_y = 4
        new_laser.rect.x = self.rect.x + (self.rect.width // 2) #starts it in middle of badguy2 ship
        new_laser.rect.y = self.rect.y + self.rect.height ##somehow starts laser from enemy 
        self.lasers.add(new_laser)

    def get_hit(self):
        if not self.is_invincible:
            self.snd_hit.play()
            if self.hp <= 0:
                self.is_invincible = True
                self.is_destroyed = True
                self.rect.x = self.rect.x - 16
                self.rect.y = self.rect.y - 16
                self.image = self.anim_explosion[self.anim_index]



    def spawn_particles(self, pos):
        new_particle = Particle()
        self.particle_group.add(new_particle)
        new_particle.rect.x = pos[0]
        new_particle.rect.y = pos[1]


