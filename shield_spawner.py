import pygame
from Shield import ShipShield
import random

class ShieldSpawner:
    def __init__(self):
        self.shipshield_group = pygame.sprite.Group()

    def update(self):
        self.shipshield_group.update()

    def spawn_shipshield(self, pos):
        new_shield = ShipShield()
        self.shipshield_group.add(new_shield)
        new_shield.rect.x = pos[0]
        new_shield.rect.y = pos[1]


