import pygame
import constance as c
from particle_spawner import ParticleSpawner
import random
from engine import Target_Engines
from Shield import TGShield



class Shipbad1(pygame.sprite.Sprite): ##this is how the ship will look and spawn
    def __init__(self):
        super(Shipbad1, self).__init__()
        self.img_explosion_01 = pygame.image.load("kb_explosion1.png").convert_alpha()
        self.img_explosion_02 = pygame.image.load("kb_explosion2.png").convert_alpha()
        self.img_explosion_03 = pygame.image.load("kb_explosion3.png").convert_alpha()
        self.img_explosion_04 = pygame.image.load("kb_explosion4.png").convert_alpha()
        self.img_explosion_05 = pygame.image.load("kb_explosion5.png").convert_alpha()
        self.img_explosion_06 = pygame.image.load("kb_explosion6.png").convert_alpha()

        self.anim_explosion = [self.img_explosion_01,
                               self.img_explosion_02,
                               self.img_explosion_03,
                               self.img_explosion_04,
                               self.img_explosion_05,
                               self.img_explosion_06]
        self.anim_index = 0
        self.turn_index = 0
        self.frame_length_max = 5
        self.frame_length = self.frame_length_max
        self.image = pygame.image.load("target_main.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width(), self.image.get_height()))
        self.rect = self.image.get_rect()
        self.is_destroyed = False
        self.is_invincible = True
        self.turning_left = False
        self.turning_right = False
        self.rect.x = random.randrange(0, ((c.display_width // 2) - 50))
        self.rect.y = 0
        self.hp_timer = random.randrange(60, 1000)
        self.hp = 1 ##this is how i will probably do reinforcement schedule. I set HP or IRT then down below, i will make it so that it will only blow up after meets irt
        self.point_value = 5
        self.ShipShield_group = pygame.sprite.Group()
        self.engine_group = pygame.sprite.Group()
        self.lasers = pygame.sprite.Group()
        self.snd_hit = pygame.mixer.Sound("tie_explosion.ogg")
        self.states = {'FLY_DOWN': 'FLY_DOWN',
                       'ATTACK': 'ATTACK'}
        self.state = self.states['FLY_DOWN']
        self.init_state = True
        self.random_num = random.randrange(-10, 400)
        self.vel_x = 0
        self.vel_y = random.randrange(1, 3)  # how fast its moving down y axis
        self.speed = 5
        img_left_01 = pygame.image.load("target_left1.png").convert_alpha()
        img_left_02 = pygame.image.load("target_left2.png").convert_alpha()
        img_left_03 = pygame.image.load("target_left3.png").convert_alpha()
        self.anim_left = [img_left_01, img_left_02, img_left_03]
        img_right_01 = pygame.image.load("target_right1.png").convert_alpha()
        img_right_02 = pygame.image.load("target_right2.png").convert_alpha()
        img_right_03 = pygame.image.load("target_right3.png").convert_alpha()
        self.anim_right = [img_right_01, img_right_02, img_right_03]

    def update(self):
        self.lasers.update()
        self.engine_group.update()
        self.ShipShield_group.update()
        if self.rect.y == 10:
            self.rev_engine()
        if self.state == 'FLY_DOWN':
            self.state_fly_down()
        elif self.state == 'ATTACK':
            self.state_attack()
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        for engine in self.engine_group:
            engine.rect.x = self.rect.x + 11
            engine.rect.y = self.rect.y - 60
        for shield in self.ShipShield_group:
            shield.rect.x = self.rect.x - 48
            shield.rect.y = self.rect.y - 30
        if self.is_destroyed:
            for shield in self.ShipShield_group:
                shield.kill()
            for engine in self.engine_group:
                engine.kill()
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
        if self.turning_left:
            max_index = 2
            if self.frame_length == 0:
                self.turn_index += 1
                if self.turn_index > max_index:
                    self.image = pygame.image.load("target_left3.png").convert_alpha()
                else:
                    self.image = self.anim_left[self.turn_index]
                    self.frame_length = self.frame_length_max
            else:
                self.frame_length -= 1
        if self.turning_right:
            max_index = 2
            if self.frame_length == 0:
                self.turn_index += 1
                if self.turn_index > max_index:
                    self.image = pygame.image.load("target_right3.png").convert_alpha()
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
        if self.rect.x <= 0:
            self.vel_x *= -1
            self.turn_index = 0
        elif self.rect.x >= 550:
            self.vel_x *= -1
            self.turn_index = 0
        if self.vel_x <= 0:
            self.turning_right = False
            self.turning_left = True
        elif self.vel_x > 0:
            self.turning_left = False
            self.turning_right = True

    def rev_engine(self):
        new_engine = Target_Engines()
        new_engine.rect.x = self.rect.x - 2
        new_engine.rect.y = self.rect.y - 5
        self.engine_group.add(new_engine)

    def engine_die(self):
        for new_engine in self.engine_group:
            self.engine_group.remove(new_engine)

    def get_hit(self):
        if not self.is_invincible:
            self.snd_hit.play()
            self.is_invincible = True
            self.is_destroyed = True
            self.hp_timer = random.randrange(60, 300)
            self.rect.x = self.rect.x - 5
            self.rect.y = self.rect.y - 5
            self.image = self.anim_explosion[self.anim_index]
        else:
            pass
            ##new_shield = TGShield()
            ##new_shield.rect.x = self.rect.x + 20
            ##new_shield.rect.y = self.rect.y
            ##self.ShipShield_group.add(new_shield)

    def new_shield(self):
        new_shield = TGShield()
        new_shield.rect.x = self.rect.x + 20
        new_shield.rect.y = self.rect.y
        self.ShipShield_group.add(new_shield)








