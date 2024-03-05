import pygame
import constance as c
from Shield import ShipShield
from engine import LEngines, REngines, LFlames, RFlames, LEngines_Red, LFlames_Red, REngines_Red, RFlames_Red
from Shield1 import ShipShield1
from Laser import LLaser, RLaser, LMuzzle, RMuzzle
from rolling import Roll_Effect
from Asteroid_HuD import Asteroid_HUD

from hud import HUD
from Score_Hud import Score_HUD




class Ship(pygame.sprite.Sprite): ## called this the initialize function
    def __init__(self):
        super(Ship, self).__init__()
        ## Shooting
        self.img_ready_01 = pygame.image.load("fire1.png").convert_alpha()
        self.img_ready_02 = pygame.image.load("fire2.png").convert_alpha()
        self.img_ready_03 = pygame.image.load("fire3.png").convert_alpha()
        self.img_ready_04 = pygame.image.load("fire4.png").convert_alpha()
        self.img_ready_05 = pygame.image.load("fire5.png").convert_alpha()
        self.img_ready_06 = pygame.image.load("fire6.png").convert_alpha()
        self.img_ready_07 = pygame.image.load("fire7.png").convert_alpha()
        self.anim_ready = [self.img_ready_01,
                           self.img_ready_02,
                           self.img_ready_03,
                           self.img_ready_04,
                           self.img_ready_05,
                           self.img_ready_06,
                           self.img_ready_07,
                           self.img_ready_06,
                           self.img_ready_05,
                           self.img_ready_04,
                           self.img_ready_03,
                           self.img_ready_02,
                           self.img_ready_01]
        self.anim_index = 0
        self.frame_length_max = 7
        self.frame_length = self.frame_length_max
        self.ShipShield_group = pygame.sprite.Group()
        self.lengine_group = pygame.sprite.Group()
        self.lflame_group = pygame.sprite.Group()
        self.rflame_group = pygame.sprite.Group()
        self.rengine_group = pygame.sprite.Group()
        self.lmuzzle_group = pygame.sprite.Group()
        self.rmuzzle_group = pygame.sprite.Group()
        self.roll_effect_group = pygame.sprite.Group()
        self.laser_timer = 10
        self.shield_timer = 5
        self.spinning = False
        self.image1 = pygame.image.load("mainship.png").convert_alpha()
        self.image_scaled = pygame.transform.scale(self.image1, (self.image1.get_width() - 10, self.image1.get_height() - 10 ))
        self.image = self.image_scaled
        self.rect = self.image_scaled.get_rect()
        self.is_invincible = False
        self.is_moving = False
        self.is_moving_x = False
        self.is_moving_y = False
        self.fire = False
        self.rect.x = c.middle_wall - 45
        self.rect.y = 605
        self.lasers = pygame.sprite.Group()
        self.snd_shoot = pygame.mixer.Sound("xwing_fire_1.ogg")
        self.lives = 3
        self.blue_flames = False
        self.red_flames = True
        self.turning_left = False
        self.turning_right = False
        self.straight = True
        self.rolling_left = False
        self.rolling_right = False
        self.kickback_timer = 30
        self.kickbacked = False
        self.hud = Score_HUD()
        self.shoot_timer = 20
        self.asteroid_hud = Asteroid_HUD()
        self.hud_group = pygame.sprite.Group()
        self.hud_group.add(self.hud)
        self.hud_group.add(self.asteroid_hud)
        self.max_hp = 3
        self.hp = 3
        self.is_alive = True
        self.max_invincible_timer = 60
        self.invincible_timer = 0
        self.snd_hit = pygame.mixer.Sound("asteroid_sound.ogg")
        self.vel_x = 0
        self.vel_y = 0
        self.speed = 7
        self.speed_timer = 300
        self.fast = False
        img_left_01 = pygame.image.load("left1.png").convert_alpha()
        img_left_01 = pygame.transform.scale(img_left_01,
                                                   (img_left_01.get_width() - 10, img_left_01.get_height() - 10))
        img_left_02 = pygame.image.load("left2.png").convert_alpha()
        img_left_02 = pygame.transform.scale(img_left_02,
                                                   (img_left_02.get_width() - 10, img_left_02.get_height() - 10))
        img_left_03 = pygame.image.load("left3.png").convert_alpha()
        img_left_03 = pygame.transform.scale(img_left_03,
                                                   (img_left_03.get_width() - 10, img_left_03.get_height() - 10))
        img_left_04 = pygame.image.load("left4.png").convert_alpha()
        img_left_04 = pygame.transform.scale(img_left_04,
                                                   (img_left_04.get_width() - 10, img_left_04.get_height() - 10))
        self.anim_left = [img_left_01, img_left_02, img_left_03, img_left_04]

        img_right_01 = pygame.image.load("right1.png").convert_alpha()
        img_right_01 = pygame.transform.scale(img_right_01,
                                                   (img_right_01.get_width() - 10, img_right_01.get_height() - 10))
        img_right_02 = pygame.image.load("right2.png").convert_alpha()
        img_right_02 = pygame.transform.scale(img_right_02,
                                                   (img_right_02.get_width() - 10, img_right_02.get_height() - 10))
        img_right_03 = pygame.image.load("right3.png").convert_alpha()
        img_right_03 = pygame.transform.scale(img_right_03,
                                                   (img_right_03.get_width() - 10, img_right_03.get_height() - 10))
        img_right_04 = pygame.image.load("right4.png").convert_alpha()
        img_right_04 = pygame.transform.scale(img_right_04,
                                                   (img_right_04.get_width() - 10, img_right_04.get_height() - 10))
        self.anim_right = [img_right_01, img_right_02, img_right_03, img_right_04]
        ## Spinning
        img_spin_01 = pygame.transform.rotate(self.image_scaled, 36)
        img_spin_02 = pygame.transform.rotate(self.image_scaled, 72)
        img_spin_03 = pygame.transform.rotate(self.image_scaled, 108)
        img_spin_04 = pygame.transform.rotate(self.image_scaled, 144)
        img_spin_05 = pygame.transform.rotate(self.image_scaled, 180)
        img_spin_06 = pygame.transform.rotate(self.image_scaled, 216)
        img_spin_07 = pygame.transform.rotate(self.image_scaled, 252)
        img_spin_08 = pygame.transform.rotate(self.image_scaled, 288)
        img_spin_09 = pygame.transform.rotate(self.image_scaled, 324)
        img_spin_10 = self.image_scaled

        self.anim_spin = [img_spin_01, img_spin_02, img_spin_03,
                          img_spin_04, img_spin_05, img_spin_06,
                          img_spin_07, img_spin_08, img_spin_09,
                          img_spin_10]
        self.spin_frame_length_max = 4
        self.spin_frame_length = self.spin_frame_length_max
        ## barrel Roll
        img_roll_01 = pygame.image.load("roll1.png").convert_alpha()
        img_roll_01 = pygame.transform.scale(img_roll_01,
                                                   (img_roll_01.get_width() - 10, img_roll_01.get_height() - 10))
        img_roll_02 = pygame.image.load("roll2.png").convert_alpha()
        img_roll_02 = pygame.transform.scale(img_roll_02,
                                                   (img_roll_02.get_width() - 10, img_roll_02.get_height() - 10))
        img_roll_03 = pygame.image.load("roll3.png").convert_alpha()
        img_roll_03 = pygame.transform.scale(img_roll_03,
                                                   (img_roll_03.get_width() - 10, img_roll_03.get_height() - 10))
        img_roll_04 = pygame.image.load("roll4.png").convert_alpha()
        img_roll_04 = pygame.transform.scale(img_roll_04,
                                                   (img_roll_04.get_width() - 10, img_roll_04.get_height() - 10))
        img_roll_05 = pygame.image.load("roll5.png").convert_alpha()
        img_roll_05 = pygame.transform.scale(img_roll_05,
                                                   (img_roll_05.get_width() - 10, img_roll_05.get_height() - 10))
        img_roll_06 = pygame.image.load("roll6.png").convert_alpha()
        img_roll_06 = pygame.transform.scale(img_roll_06,
                                                   (img_roll_06.get_width() - 10, img_roll_06.get_height() - 10))
        img_roll_07 = pygame.image.load("roll7.png").convert_alpha()
        img_roll_07 = pygame.transform.scale(img_roll_07,
                                                   (img_roll_07.get_width() - 10, img_roll_07.get_height() - 10))
        img_roll_08 = pygame.image.load("roll8.png").convert_alpha()
        img_roll_08 = pygame.transform.scale(img_roll_08,
                                                   (img_roll_08.get_width() - 10, img_roll_08.get_height() - 10))
        img_roll_09 = pygame.image.load("roll9.png").convert_alpha()
        img_roll_09 = pygame.transform.scale(img_roll_09,
                                                   (img_roll_09.get_width() - 10, img_roll_09.get_height() - 10))
        img_roll_010 = pygame.image.load("roll10.png").convert_alpha()
        img_roll_010 = pygame.transform.scale(img_roll_010,
                                                   (img_roll_010.get_width() - 10, img_roll_010.get_height() - 10))
        img_roll_011 = pygame.image.load("roll11.png").convert_alpha()
        img_roll_011 = pygame.transform.scale(img_roll_011,
                                                   (img_roll_011.get_width() - 10, img_roll_011.get_height() - 10))
        img_roll_012 = pygame.image.load("roll12.png").convert_alpha()
        img_roll_012 = pygame.transform.scale(img_roll_012,
                                                   (img_roll_012.get_width() - 10, img_roll_012.get_height() - 10))
        img_roll_013 = pygame.image.load("roll13.png").convert_alpha()
        img_roll_013 = pygame.transform.scale(img_roll_013,
                                                   (img_roll_013.get_width() - 10, img_roll_013.get_height() - 10))
        self.anim_roll_left = [img_left_01, img_left_02, img_left_03, img_left_04, img_roll_01, img_roll_02,
                          img_roll_03, img_roll_04, img_roll_05, img_roll_06, img_roll_07, img_roll_08,
                          img_roll_09, img_roll_010, img_roll_011, img_roll_012, img_roll_013, img_right_04,
                          img_right_03, img_right_02, img_right_01, img_spin_10]
        self.anim_roll_right = [img_right_01, img_right_02, img_right_03, img_right_04, img_roll_013, img_roll_012,
                          img_roll_011, img_roll_010, img_roll_09, img_roll_08, img_roll_07, img_roll_06,
                          img_roll_05, img_roll_04, img_roll_03, img_roll_02, img_roll_01, img_left_04,
                          img_left_03, img_left_02, img_left_01, img_spin_10]
        self.roll_frame_length_max = 2
        self.roll_frame_length = self.roll_frame_length_max
        self.laser_x_pad = 3







    def update(self):
        self.lasers.update()
        self.hud_group.update()
        self.lmuzzle_group.update()
        self.rmuzzle_group.update()
        self.lengine_group.update()
        self.lflame_group.update()
        self.rflame_group.update()
        self.rengine_group.update()
        self.ShipShield_group.update()
        self.roll_effect_group.update()
        self.laser_timer -= 1
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        if self.kickbacked:
            self.is_invincible = True
            if self.kickback_timer == 0:
                self.kickbacked = False
                self.is_invincible = False

                self.kickback_timer = 20
            else:
                self.kickback_timer -= 1
        if self.fast:
            self.speed = 14
            self.speed_timer -= 1
            if self.speed_timer == 0:
                self.fast = False
                self.speed_timer = 300
        if not self.fast:
            self.speed = 6
        for new_effect in self.roll_effect_group:
            new_effect.rect.x = self.rect.x - 290
            new_effect.rect.y = self.rect.y - 350
        for shield in self.ShipShield_group:
            shield.rect.x = self.rect.x - 53
            shield.rect.y = self.rect.y - 35
        for engine in self.lengine_group:
            engine.rect.x = self.rect.x - 3
            engine.rect.y = self.rect.y + 98
        for flame in self.lflame_group:
            flame.rect.x = self.rect.x - 11
            flame.rect.y = self.rect.y + 107
        for flame in self.rflame_group:
            flame.rect.x = self.rect.x + 45
            flame.rect.y = self.rect.y + 107
        for engine in self.rengine_group:
            engine.rect.x = self.rect.x + 37
            engine.rect.y = self.rect.y + 98

        for laser in self.lasers:
            if laser.rect.y <= 0:
                self.lasers.remove(laser)
        for lmuzzle in self.lmuzzle_group:
            lmuzzle.rect.x = self.rect.x + 23
            lmuzzle.rect.y = self.rect.y - 18
        for rmuzzle in self.rmuzzle_group:
            rmuzzle.rect.x = self.rect.x + 48
            rmuzzle.rect.y = self.rect.y - 18
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= c.display_width - self.rect.width:
            self.rect.x = c.display_width - self.rect.width
        if self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.y >= c.display_height - self.rect.height:
            self.rect.y = c.display_height - self.rect.height
        if self.turning_left:
            max_index = len(self.anim_left) - 1
            if self.frame_length == 0:
                self.anim_index += 1
                if self.anim_index > max_index:
                    self.anim_index = max_index
                else:
                    self.image = self.anim_left[self.anim_index]
                    self.frame_length = self.frame_length_max
            else:
                self.frame_length -= 1
        if self.turning_right:
            max_index = len(self.anim_right) - 1
            if self.frame_length == 0:
                self.anim_index += 1
                if self.anim_index > max_index:
                    self.anim_index = max_index
                else:
                    self.image = self.anim_right[self.anim_index]
                    self.frame_length = self.frame_length_max
            else:
                self.frame_length -= 1
        if self.spinning:
            self.engine_die()
            max_index = len(self.anim_spin) - 1
            if self.spin_frame_length == 0:
                self.anim_index += 1
                if self.anim_index > max_index:
                    self.spinning = False
                else:
                    self.image = self.anim_spin[self.anim_index]
                    self.spin_frame_length = self.spin_frame_length_max
            else:
                self.spin_frame_length -= 1
        if self.rolling_left:
            self.engine_die()
            max_index = len(self.anim_roll_left) - 1
            if self.roll_frame_length == 0:
                self.anim_index += 1
                if self.anim_index > max_index:
                    self.rolling_left = False
                    self.kill_roll_effect()
                else:
                    self.image = self.anim_roll_left[self.anim_index]
                    self.roll_frame_length = self.roll_frame_length_max
            else:
                self.roll_frame_length -= 1
        if self.rolling_right:
            self.engine_die()
            max_index = len(self.anim_roll_right) - 1
            if self.roll_frame_length == 0:
                self.anim_index += 1
                if self.anim_index > max_index:
                    self.rolling_right = False
                else:
                    self.image = self.anim_roll_right[self.anim_index]
                    self.roll_frame_length = self.roll_frame_length_max
            else:
                self.roll_frame_length -= 1






    def start_shields(self):
        new_shield = ShipShield()
        new_shield.rect.x = self.rect.x + 16
        new_shield.rect.y = self.rect.y
        self.ShipShield_group.add(new_shield)



    def turn_left(self):
        self.image = pygame.image.load("left4.png").convert_alpha()

    def turn_right(self):
        self.image = pygame.image.load("right4.png").convert_alpha()

    def go_straight(self):
        self.image = self.image_scaled




    def get_hit(self):
        self.snd_hit.play()
        new_shield = ShipShield()
        new_shield.rect.x = self.rect.x + 16
        new_shield.rect.y = self.rect.y
        self.ShipShield_group.add(new_shield)

    def rev_engine(self):
        if self.red_flames:
            new_lengine = LEngines_Red()
            new_lengine.rect.x = self.rect.x
            new_lengine.rect.y = self.rect.y
            self.lengine_group.add(new_lengine)
            new_flame = LFlames_Red()
            self.lflame_group.add(new_flame)
            new_flame = RFlames_Red()
            self.rflame_group.add(new_flame)
            new_rengine = REngines_Red()
            new_rengine.rect.x = self.rect.x
            new_rengine.rect.y = self.rect.y
            self.rengine_group.add(new_rengine)
        elif self.blue_flames:
            new_lengine = LEngines()
            new_lengine.rect.x = self.rect.x
            new_lengine.rect.y = self.rect.y
            self.lengine_group.add(new_lengine)
            new_flame = LFlames()
            self.lflame_group.add(new_flame)
            new_flame = RFlames()
            self.rflame_group.add(new_flame)
            new_rengine = REngines()
            new_rengine.rect.x = self.rect.x
            new_rengine.rect.y = self.rect.y
            self.rengine_group.add(new_rengine)

    def engine_die(self):
        for new_lengine in self.lengine_group:
            self.lengine_group.remove(new_lengine)
        for new_flame in self.lflame_group:
            self.lflame_group.remove(new_flame)
        for new_rengine in self.rengine_group:
            self.rengine_group.remove(new_rengine)
        for new_flame in self.rflame_group:
            self.rflame_group.remove(new_flame)

    def start_roll_effect(self):
        new_effect = Roll_Effect()
        new_effect.rect.x = self.rect.x
        new_effect.rect.y = self.rect.y
        self.roll_effect_group.add(new_effect)

    def kill_roll_effect(self):
        for new_effect in self.roll_effect_group:
            self.roll_effect_group.remove(new_effect)
            self.roll_effect_group.anim_index = 0




    def shoot(self):
        if self.laser_timer <= 0:
            ##self.snd_shoot.play()
            new_lmuzzle = LMuzzle()
            new_lmuzzle.rect.x = self.rect.x + 45
            new_lmuzzle.rect.y = self.rect.y
            self.lmuzzle_group.add(new_lmuzzle)
            new_rmuzzle = RMuzzle()
            new_rmuzzle.rect.x = self.rect.x
            new_rmuzzle.rect.y = self.rect.y
            self.rmuzzle_group.add(new_rmuzzle)
            new_llaser = LLaser()
            new_llaser.rect.x = self.rect.x + 40
            new_llaser.rect.y = self.rect.y + 10
            self.lasers.add(new_llaser)
           ## new_rlaser = RLaser()
            ##new_rlaser.rect.x = self.rect.x + 50
            ##new_rlaser.rect.y = self.rect.y - 10
            ##self.lasers.add(new_rlaser)
            self.laser_timer = 10
        else:
            self.laser_timer -= 1




    def death(self):
        self.lives -= 1
        print(f'lives: {self.lives}')
        if self.lives <= 0:
            self.lives = 0
            self.is_alive = False
            self.image = pygame.Surface((0, 0))
        self.hp = self.max_hp
        self.hud.lives.decrement_life()
        self.is_invincible = True
        self.invincible_timer = self.max_invincible_timer


