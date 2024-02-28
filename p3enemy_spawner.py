import pygame
import constance as c
from p3badguy1 import Shipbad1
from p3badguy2 import ShipBad2
from sdeltaasteroid import SdeltaAsteroid
import random
from spin import Spin_Icon, Speed_boost, Max_gems, Roll_Icon
class p3EnemySpawner: ##this is when it will spawn
    def __init__(self):
        self.enemy_group1 = pygame.sprite.Group()
        self.enemy_group2 = pygame.sprite.Group()
        self.spin_group = pygame.sprite.Group()
        self.max_gems_group = pygame.sprite.Group()
        self.speed_group = pygame.sprite.Group()
        self.sdeltaasteroid_group = pygame.sprite.Group()
        self.spawn_timer = random.randrange(30, 120)
        self.asteroid_timer = random.randrange(60, 180)
        self.asteroid_list = []
        self.remove_timer = 300
        self.normal_generate = True
        self.max_generate = False
        self.roll_group = pygame.sprite.Group()
        self.roll_timer = random.randrange(10, 20)
        self.max_num_enemy1 = 1
        self.max_num_enemy2 = 1
        self.spin_timer = random.randrange(50, 100)
        self.speed_timer = random.randrange(100, 2000)
        self.max_gems_timer = random.randrange(100, 2000)
        self.current_num_enemy1 = 0
        self.current_num_enemy2 = 0

    def update(self): ## this is what defines the update function in the main file
        self.enemy_group2.update()
        self.enemy_group1.update()
        if self.max_generate:
            self.remove_timer -= 1
            if self.remove_timer == 0:
                self.max_generate = False
                self.remove_timer = 300
        for enemy in self.enemy_group1:
            if enemy.rect.y >= c.display_height:
                self.enemy_group1.remove(enemy)
            elif enemy.is_destroyed == True:
                if self.spawn_timer == 0:
                    self.enemy1_alive = False
                    self.current_num_enemy1 -= 1
                    self.enemy_group1.remove(enemy)
                else:
                    self.spawn_timer -= 1
        if self.current_num_enemy1 >= self.max_num_enemy1:
            pass
        else:
            new_enemy1 = Shipbad1()
            self.enemy_group1.add(new_enemy1)
            self.current_num_enemy1 += 1
            self.spawn_timer = 30

        for enemy in self.enemy_group2:
            if enemy.rect.y >= c.display_height:
                self.enemy_group2.remove(enemy)
            if enemy.is_destroyed == True:
                if self.spawn_timer == 0:
                    self.enemy2_alive = False
                    self.current_num_enemy2 -= 1
                    self.enemy_group2.remove(enemy)
                else:
                    self.spawn_timer -= 1

        if self.current_num_enemy2 >= self.max_num_enemy2:
            pass
        else:
            new_enemy2 = ShipBad2()
            self.enemy_group2.add(new_enemy2)
            self.current_num_enemy2 += 1
            self.spawn_timer = 30

        self.spin_group.update()
        if self.spin_timer == 0:
            new_spin = Spin_Icon()
            self.spin_group.add(new_spin)
            self.spin_timer = random.randrange(500, 1000)
        else:
            self.spin_timer -= 1

        self.speed_group.update()
        if self.speed_timer == 0:
            new_speed = Speed_boost()
            self.speed_group.add(new_speed)
            self.speed_timer = random.randrange(700, 1000)
        else:
            self.speed_timer -= 1

        self.max_gems_group.update()
        if not self.max_generate:
            if self.max_gems_timer == 0:
                new_max = Max_gems()
                self.max_gems_group.add(new_max)
                self.max_gems_timer = random.randrange(900, 1500)
            else:
                self.max_gems_timer -= 1

        self.roll_group.update()
        if self.roll_timer == 0:
            new_roll = Roll_Icon()
            self.roll_group.add(new_roll)
            self.roll_timer = random.randrange(500, 1000)
        else:
            self.roll_timer -= 1

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

        self.sdeltaasteroid_group.update()
        for asteroid in self.sdeltaasteroid_group:
            if asteroid.rect.y > c.display_height:
                self.sdeltaasteroid_group.remove(asteroid)

        if self.asteroid_timer == 0:
            new_asteroid = SdeltaAsteroid()
            self.sdeltaasteroid_group.add(new_asteroid)
            self.asteroid_list.append('e')
            if self.normal_generate:
                self.asteroid_timer = random.randrange(60, 150)
            if self.max_generate:
                self.asteroid_timer = random.randrange(5, 10)
        self.asteroid_timer -= 1






   ### def spawn_enemy(self):
      ##  random_number = random.randrange(0,100)
        ##if random_number <= 50:
          ##  new_enemy = Shipbad1()
        ##elif random_number >= 50:
          ##  new_enemy = ShipBad2()
        ## self.enemy_group.add(new_enemy)

    def clear_enemies(self):
        for enemy in self.enemy_group1:
            enemy.kill()
        for enemy in self.enemy_group2:
            enemy.kill()
        for enemy in self.sdeltaasteroid_group:
            enemy.kill()