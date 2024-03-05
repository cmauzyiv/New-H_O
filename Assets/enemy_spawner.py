import pygame
import constance as c
from badguy1 import Shipbad1
from P2badguy2 import ShipBad2
from spritesheet import Shipbad3
from asteroid import Asteroid
from p2asteroid import P2Asteroid
from sdeltaasteroid import SdeltaAsteroid
from Asteroid_Powerups import Yellow_Icon, Blue_Icon, Red_Icon
import random
from spin import Spin_Icon, Speed_boost, Max_gems, Roll_Icon, Red_Flame, Blue_Flame


class EnemySpawner: ##this is when it will spawn
    def __init__(self):
        self.enemy_group1 = pygame.sprite.Group()
        self.enemy_group2 = pygame.sprite.Group()
        self.enemy_group3 = pygame.sprite.Group()
        self.asteroid_group = pygame.sprite.Group()
        self.spin_group = pygame.sprite.Group()
        self.yasteroid_group = pygame.sprite.Group()
        self.basteroid_group = pygame.sprite.Group()
        self.rasteroid_group = pygame.sprite.Group()
        self.red_flame_group = pygame.sprite.Group()
        self.blue_flame_group = pygame.sprite.Group()
        self.speed_group = pygame.sprite.Group()
        self.max_gems_group = pygame.sprite.Group()
        self.roll_group = pygame.sprite.Group()
        self.roll_timer = random.randrange(10, 20)
        self.p1_asteroid_group = pygame.sprite.Group()
        self.yellow_icon_group = pygame.sprite.Group()
        self.blue_icon_group = pygame.sprite.Group()
        self.red_icon_group = pygame.sprite.Group()
        self.p2_asteroid_group = pygame.sprite.Group()
        self.p3_asteroid_group = pygame.sprite.Group()
        self.phase = 1
        self.asteroid_list = []
        self.red_flames = True
        self.blue_flames = False
        self.normal_generate = True
        self.max_generate = False
        self.yellow_gems = False
        self.blue_gems = False
        self.red_gems = False
        self.spawn_timer = random.randrange(30, 120)
        self.remove_timer = 300
        self.asteroid_timer = random.randrange(60, 150)
        self.spin_timer = random.randrange(700, 1000)
        self.speed_timer = random.randrange(400, 2000)
        self.max_gems_timer = random.randrange(500, 2000)
        self.icon_timer = random.randrange(100, 1000)
        self.flame_timer = random.randrange(300, 1200)
        self.max_num_enemy1 = 1
        self.max_num_enemy2 = 1
        self.max_num_enemy3 = 1
        self.current_num_enemy1 = 0
        self.current_num_enemy2 = 0
        self.current_num_enemy3 = 0

    def update(self): ## this is what defines the update function in the main file
        self.enemy_group1.update()
        self.enemy_group2.update()
        self.enemy_group3.update()
        self.p2_asteroid_group.update()
        self.p3_asteroid_group.update()
        self.yellow_icon_group.update()
        self.blue_icon_group.update()
        self.red_icon_group.update()
        self.yasteroid_group.update()
        self.basteroid_group.update()
        self.rasteroid_group.update()
        self.red_flame_group.update()
        self.blue_flame_group.update()
        if self.max_generate:
            self.remove_timer -= 1
            if self.remove_timer == 0:
                self.max_generate = False
                self.remove_timer = 300
        for enemy in self.enemy_group1:
            if enemy.rect.y >= c.display_height:
                self.enemy_group1.remove(enemy)
            elif enemy.dead == True:
                self.current_num_enemy1 -= 1
                self.enemy_group1.remove(enemy)

        if self.current_num_enemy1 >= self.max_num_enemy1:
            pass
        else:
            new_enemy1 = Shipbad1()
            self.enemy_group1.add(new_enemy1)
            self.current_num_enemy1 += 1
            self.spawn_timer = 30


        if not self.phase == 1:
            if self.current_num_enemy2 >= self.max_num_enemy2:
                pass
            else:
                new_enemy2 = ShipBad2()
                self.enemy_group2.add(new_enemy2)
                self.current_num_enemy2 += 1
                self.spawn_timer = 30

        for enemy in self.enemy_group2:
            if enemy.rect.y >= c.display_height:
                self.enemy_group2.remove(enemy)
            elif enemy.dead == True:
                self.current_num_enemy2 -= 1
                self.enemy_group2.remove(enemy)



        self.spin_group.update()
        if self.spin_timer == 0:
            new_spin = Spin_Icon()
            self.spin_group.add(new_spin)
            self.spin_timer = random.randrange(700, 2000)
        else:
            self.spin_timer -= 1

        self.speed_group.update()
        if self.speed_timer == 0:
            new_speed = Speed_boost()
            self.speed_group.add(new_speed)
            self.speed_timer = random.randrange(1000, 3000)
        else:
            self.speed_timer -= 1

        self.max_gems_group.update()
        if not self.max_generate:
            if self.max_gems_timer == 0:
                new_max = Max_gems()
                self.max_gems_group.add(new_max)
                self.max_gems_timer = random.randrange(1000, 3500)
            else:
                self.max_gems_timer -= 1

        self.roll_group.update()
        if self.roll_timer == 0:
            new_roll = Roll_Icon()
            self.roll_group.add(new_roll)
            self.roll_timer = random.randrange(600, 1000)
        else:
            self.roll_timer -= 1


        if self.icon_timer == 0:
            self.spawn_icon()
            self.icon_timer = random.randrange(1000, 3000)
        else:
            self.icon_timer -= 1


        if self.flame_timer == 0:
            self.spawn_flames()
            self.flame_timer = random.randrange(1000, 3000)
        else:
            self.flame_timer -= 1


        for flames in self.blue_flame_group:
            if flames.rect.y >= c.display_height:
                self.blue_flame_group.remove(flames)

        for flames in self.red_flame_group:
            if flames.rect.y >= c.display_height:
                self.red_flame_group.remove(flames)

        for new_roll in self.roll_group:
            if new_roll.rect.y >= c.display_height:
                self.roll_group.remove(new_roll)

        for new_max in self.max_gems_group:
            if new_max.rect.y >= c.display_height:
                self.max_gems_group.remove(new_max)

        for new_speed in self.speed_group:
            if new_speed.rect.y >= c.display_height:
                self.speed_group.remove(new_speed)

        for new_spin in self.spin_group:
            if new_spin.rect.y >= c.display_height:
                self.speed_group.remove(new_spin)



        for asteroid in self.asteroid_group:
            if asteroid.rect.y >= c.display_height:
                self.asteroid_group.remove(asteroid)


        if self.asteroid_timer == 0:
            if self.yellow_gems:
                asteroid = Asteroid()
                self.asteroid_group.add(asteroid)
                self.yasteroid_group.add(asteroid)
            if self.blue_gems:
                asteroid = P2Asteroid()
                self.asteroid_group.add(asteroid)
                self.basteroid_group.add(asteroid)
            if self.red_gems:
                asteroid = SdeltaAsteroid()
                self.asteroid_group.add(asteroid)
                self.rasteroid_group.add(asteroid)
            else:
                self.asteroid_timer = random.randrange(60, 150)
            if self.normal_generate:
                self.asteroid_timer = random.randrange(60, 150)
            if self.max_generate:
                self.asteroid_timer = random.randrange(5, 10)
        self.asteroid_timer -= 1


        for asteroid in self.asteroid_group:
            if asteroid.rect.y > c.display_height:
                self.asteroid_group.remove(asteroid)
                self.asteroid_list.remove('e')

        self.asteroid_group.update()







    def spawn_icon(self):
        random_number = random.randrange(0,100)
        if self.yellow_gems:
            if random_number <= 50:
                new_icon = Blue_Icon()
                self.blue_icon_group.add(new_icon)
            elif random_number >= 51:
                new_icon = Red_Icon()
                self.red_icon_group.add(new_icon)
        elif self.red_gems:
            if random_number <= 50:
                new_icon = Blue_Icon()
                self.blue_icon_group.add(new_icon)
            elif random_number >= 51:
                new_icon = Yellow_Icon()
                self.yellow_icon_group.add(new_icon)
        elif self.blue_gems:
            if random_number <= 50:
                new_icon = Red_Icon()
                self.red_icon_group.add(new_icon)
            elif random_number >= 51:
                new_icon = Yellow_Icon()
                self.yellow_icon_group.add(new_icon)
        else:
            if random_number <= 32:
                new_icon = Blue_Icon()
                self.blue_icon_group.add(new_icon)
            elif 33 < random_number < 66:
                new_icon = Yellow_Icon()
                self.yellow_icon_group.add(new_icon)
            elif random_number >= 67:
                new_icon = Red_Icon()
                self.red_icon_group.add(new_icon)



    def spawn_flames(self):
        if self.red_flames:
            new_flames = Blue_Flame()
            self.blue_flame_group.add(new_flames)
        elif self.blue_flames:
            new_flames = Red_Flame()
            self.red_flame_group.add(new_flames)



    def clear_yasteroids(self):
        for asteroid in self.asteroid_group:
            asteroid.kill()

    def clear_enemies(self):
        for enemy in self.enemy_group1:
            enemy.kill()
        for enemy in self.asteroid_group:
            enemy.kill()
