import pygame
from Explosions import ShipExplosions, P1AsteroidExplosions, P2AsteroidExplosions, SdAsteroidExplosions, SdeltaAsteroidExplosions
import random

class ExplosionSpawner:
    def __init__(self):
        self.shipexplosions_group = pygame.sprite.Group()
        self.p1asteroidexplosions_group = pygame.sprite.Group()
        self.p2asteroidexplosions_group = pygame.sprite.Group()
        self.sdasteroidexplosions_group = pygame.sprite.Group()
        self.sdeltaasteroidexplosions_group = pygame.sprite.Group()


    def update(self):
        self.shipexplosions_group.update()
        self.p1asteroidexplosions_group.update()
        self.p2asteroidexplosions_group.update()
        self.sdasteroidexplosions_group.update()



    def spawn_shipexplosions(self, pos):
        new_explosion = ShipExplosions()
        self.shipexplosions_group.add(new_explosion)
        new_explosion.rect.x = pos[0]
        new_explosion.rect.y = pos[1]

    def spawn_p1asteroidexplosions(self, pos):
        new_explosion = P1AsteroidExplosions()
        self.p1asteroidexplosions_group.add(new_explosion)
        new_explosion.rect.x = pos[0]
        new_explosion.rect.y = pos[1]

    def spawn_p2asteroidexplosions(self, pos):
        new_explosion = P2AsteroidExplosions()
        self.p2asteroidexplosions_group.add(new_explosion)
        new_explosion.rect.x = pos[0]
        new_explosion.rect.y = pos[1]

    def spawn_Sdasteroidexplosions(self, pos):
        new_explosion = SdAsteroidExplosions()
        self.sdasteroidexplosions_group.add(new_explosion)
        new_explosion.rect.x = pos[0]
        new_explosion.rect.y = pos[1]

    def spawn_Sdeltaasteroidexplosions(self, pos):
        new_explosion = SdeltaAsteroidExplosions()
        self.sdasteroidexplosions_group.add(new_explosion)
        new_explosion.rect.x = pos[0]
        new_explosion.rect.y = pos[1]



