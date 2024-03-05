import pygame
import pygame
from badguy1 import Shipbad1
from badguy2 import ShipBad2
import constance as c
from background import BG, BG1
from ship import Ship
from enemy_spawner import EnemySpawner
from p2enemy_spawner import p2EnemySpawner
from particle_spawner import ParticleSpawner
from event_handler import EventHandler

class PlayerBehaviorRecorder:
    def __init__(self, filename):
        self.player = pygame.sprite.Group()
        self.lasers = pygame.sprite.Group()
        self.enemy_group1 = pygame.sprite.Group()
        self.enemy_group2 = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.collisions =
        self.trial_num = 0
        self.phase_num = 0

        self.filename = filename
        self.file = open("data.txt", "w")


    def record_data(self, event, actor):

        class PlayerBehaviorRecorder:
            def __init__(self, filename):
                self.player = player
                self.lasers = pygame.sprite.Group()
                self.enemy_group1 = pygame.sprite.Group()
                self.enemy_group2 = pygame.sprite.Group()
                self.asteroids = pygame.sprite.Group()
                self.trial_num = 0
                self.phase_num = phase_num
                self.trial_num = trial_num
                self.trial_type = trial_type
                self.alt_1 = alt_1
                self.tg_1 = tg_1
                self.filename = filename
                self.file = open("data.txt", "w")
                self.tg_1 = 0
                self.alt_1 = 0




    def record_data(self, event):
        fw.write('\n')
        fw.write('phase = ')
        if phase_num = 1:
            fw.write('1')
        elif phase_num == 2:
            fw.write('2')
        else:
            fw.write(str(phase))
            fw.write('\n')
            fw.write('trial = ')
            fw.write(str(trial))
            fw.write('\n')
            fw.write('target = ')
            fw.write(str(target_clicks))
            fw.write('\n')

            if trial_type == 0:
                fw.write('Baseline')
                fw.write('\n')
                fw.write(str(target_clicks))
                fw.write('\n')

            elif trial_type == 2:
                fw.write('Alternative 2')
                fw.write('\n')
                fw.write(str(alt_2))
                fw.write('\n')


            elif trial_type == 1:
                fw.write('Alternative 1')
                fw.write('\n')
                fw.write(str(alt_1))
                fw.write('\n')

                def record_data():
                    fw.write(str(event) + "\n")
                    f.write('phase = ')
                    if self.phase_num == 1:
                        self.file.write('1')
                    elif self.phase_num == 2:
                        self.file.write('2')
                    else:
                        self.file.write(str(phase_num))
                        self.file.write('\n')
                        self.file.write('trial = ')
                        self.file.write(str(trial_num))
                        self.file.write('\n')
                        self.file.write('target = ')
                        self.file.write(str(tg_1))
                        self.file.write('\n')
                        self.file.write(str(alt_1))
                        self.file.write('\n')