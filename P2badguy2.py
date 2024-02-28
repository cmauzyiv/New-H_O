import pygame
import constance as c
from particle_spawner import ParticleSpawner
import random
from engine import Alt_Engines
from Shield import AltShield
from particle import Particle





class ShipBad2(pygame.sprite.Sprite): ##this is how the ship will look and spawn
    def __init__(self):
        super(ShipBad2, self).__init__()
        self.img_explosion_01 = pygame.image.load("alt_explosion1.png").convert_alpha()
        self.img_explosion_02 = pygame.image.load("alt_explosion2.png").convert_alpha()
        self.img_explosion_03 = pygame.image.load("alt_explosion3.png").convert_alpha()
        self.img_explosion_04 = pygame.image.load("alt_explosion4.png").convert_alpha()
        self.img_explosion_05 = pygame.image.load("alt_explosion5.png").convert_alpha()
        self.img_explosion_06 = pygame.image.load("alt_explosion6.png").convert_alpha()
        self.img_explosion_07 = pygame.image.load("alt_explosion7.png").convert_alpha()
        self.img_explosion_08 = pygame.image.load("alt_explosion8.png").convert_alpha()
        self.img_explosion_09 = pygame.image.load("alt_explosion9.png").convert_alpha()

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
        self.image = pygame.image.load("alt_main.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() - 10, self.image.get_height() - 10))
        self.rect = self.image.get_rect()
        self.is_destroyed = False
        self.is_invincible = True
        ##if i wanted to have him randomly appear somewhere (basically for when i have it respawn)
        self.rect.x = random.randrange((c.middle_wall + 5), (c.right_wall - self.rect.width))
        self.rect.y = 0
        self.hp = 1 ##this is how i will probably do reinforcement schedule. I set HP or IRT then down below, i will make it so that it will only blow up after meets irt
        self.hp_timer = random.randrange(60, 300)
        self.lasers = pygame.sprite.Group()
        self.laser_timer_max = 60
        self.laser_timer = self.laser_timer_max
        self.states = {'FLY_DOWN': 'FLY_DOWN',
                       'ATTACK': 'ATTACK'}
        self.state = self.states['FLY_DOWN']
        self.init_state = True
        self.point_value = 5
        self.engine_group = pygame.sprite.Group()
        self.ShipShield_group = pygame.sprite.Group()
        self.random_num = random.randrange(-10, 400)
        self.snd_hit = pygame.mixer.Sound("ding.ogg")
        self.vel_x = 0
        self.vel_y = random.randrange(1, 3) #how fast its moving down y axis
        self.speed = 5
        img_left_01 = pygame.image.load("alt_left1.png").convert_alpha()
        img_left_02 = pygame.image.load("alt_left2.png").convert_alpha()
        img_left_03 = pygame.image.load("alt_left3.png").convert_alpha()
        self.anim_left = [img_left_01, img_left_02, img_left_03]
        img_right_01 = pygame.image.load("alt_right1.png").convert_alpha()
        img_right_02 = pygame.image.load("alt_right2.png").convert_alpha()
        img_right_03 = pygame.image.load("alt_right3.png").convert_alpha()
        self.anim_right = [img_right_01, img_right_02, img_right_03]
        self.turn_index = 0
        self.turning_left = False
        self.turning_right = False
        self.dead = False

    def update(self):
        self.lasers.update()
        self.engine_group.update()
        self.ShipShield_group.update()
        self.particle_group.update()
        if self.rect.y == 10:
            self.rev_engine()
        for engine in self.engine_group:
            engine.rect.x = self.rect.x + 7
            engine.rect.y = self.rect.y - 68
        for shield in self.ShipShield_group:
            shield.rect.x = self.rect.x - 55
            shield.rect.y = self.rect.y - 35
        for hit_fx in self.particle_group:
            hit_fx.rect.x += self.vel_x
            hit_fx.rect.y += self.vel_y
        if self.state == 'FLY_DOWN':
            self.state_fly_down()
        elif self.state == 'ATTACK':
            self.state_attack()
        self.hp_timer -= 1
        if self.hp_timer == 0:
            self.is_invincible = False
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        if self.is_destroyed:
            for shield in self.ShipShield_group:
                shield.kill()
            for engine in self.engine_group:
                engine.kill()
            self.turning_left = False
            self.turning_right = False
            max_index = len(self.anim_explosion) - 1
            if self.frame_length == 0:
                self.anim_index += 1
                if self.anim_index > max_index:
                    self.dead = True
                else:
                    self.image = self.anim_explosion[self.anim_index]
                    self.frame_length = self.frame_length_max
            else:
                self.frame_length -= 1
        if self.turning_left:
            max_index = 2
            if self.frame_length == 0:
                self.turn_index += 1
                if self.turn_index > max_index:
                    self.image = pygame.image.load("alt_left3.png").convert_alpha()
                else:
                    self.image = self.anim_left[self.turn_index]
                    self.frame_length = self.frame_length_max
            else:
                self.frame_length -= 1

        elif self.turning_right:
            max_index = 2
            if self.frame_length == 0:
                self.turn_index += 1
                if self.turn_index > max_index:
                    self.image = pygame.image.load("alt_right3.png").convert_alpha()
                else:
                    self.image = self.anim_right[self.turn_index]
                    self.frame_length = self.frame_length_max
            else:
                self.frame_length -= 1

    def state_fly_down(self):
        if self.init_state:
            self.init_state = False
        if self.rect.y >= self.random_num:
            self.state = self.states['ATTACK']
            self.init_state = True
        if self.rect.y >= c.display_height - self.rect.height:
            self.vel_y *= -1
        if self.rect.y <= -11:
            self.vel_y *= -1

    def state_attack(self):
        self.engine_die()
        if self.init_state:
            self.vel_y = 0
            while self.vel_x == 0:
                self.vel_x = random.randrange(3, 4)
            self.init_state = False
        if self.rect.x <= c.middle_wall + 1:
            self.vel_x *= -1
            self.turn_index = 0
        elif self.rect.x >= c.display_width - self.rect.width:
            self.vel_x *= -1
            self.turn_index = 0
        if self.vel_x <= 0:
            self.turning_right = False
            self.turning_left = True
        elif self.vel_x > 0:
            self.turning_left = False
            self.turning_right = True

    def rev_engine(self):
        new_engine = Alt_Engines()
        new_engine.rect.x = self.rect.x - 4
        new_engine.rect.y = self.rect.y - 1
        self.engine_group.add(new_engine)

    def engine_die(self):
        for new_engine in self.engine_group:
            self.engine_group.remove(new_engine)

    def get_hit(self):
        if not self.is_invincible:
            ##self.snd_hit.play()
            self.is_invincible = True
            self.is_destroyed = True
            self.hp_timer = random.randrange(60, 300)
            self.rect.x = self.rect.x - 120
            self.rect.y = self.rect.y - 75
            self.image = self.anim_explosion[self.anim_index]
        else:

            new_shield = AltShield()
            new_shield.rect.x = self.rect.x + 20
            new_shield.rect.y = self.rect.y
            self.ShipShield_group.add(new_shield)

    def new_shield(self):
        new_shield = AltShield()
        new_shield.rect.x = self.rect.x + 20
        new_shield.rect.y = self.rect.y
        self.ShipShield_group.add(new_shield)

    def spawn_particles(self, pos):
        new_particle = Particle()
        self.particle_group.add(new_particle)
        new_particle.rect.x = pos[0]
        new_particle.rect.y = pos[1]





