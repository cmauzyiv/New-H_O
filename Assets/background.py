import pygame
import constance as c
from star import Star
import random
from planet import Planet

class BG1(pygame.sprite.Sprite):
    def __init__(self):
        super(BG1, self).__init__()
        self.image = pygame.Surface(c.display_size)
        self.color = (0, 50, 100) ##other bg options (0, 50, 100)- blue
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.stars = pygame.sprite.Group()
        self.planets = pygame.sprite.Group()
        self.star_timer = random.randrange(1, 10)
        self.random_timer_range_low = 120
        self.random_timer_range_high = 360
        self.planet_timer = random.randrange(self.random_timer_range_low, self.random_timer_range_high)
        self.max_planets = 1
        self.current_num_planets = 0


    def update(self):
        self.planets.update()
        for planet in self.planets:
            if planet.rect.y > c.display_height:
                self.planets.remove(planet)
                self.current_num_planets -= 1

                self.planet_timer = random.randrange(self.random_timer_range_low, self.random_timer_range_high)
        if self.planet_timer == 0:
            if self.current_num_planets <= self.max_planets:
                new_planet = Planet()
                self.planets.add(new_planet)
                self.current_num_planets += 1
                self.planet_timer = random.randrange(self.random_timer_range_low, self.random_timer_range_high)

        self.stars.update()
        for star in self.stars:
            if star.rect.y >= c.display_height:
                self.stars.remove(star)
        if self.star_timer == 0:
            new_star = Star()
            self.stars.add(new_star)
            self.star_timer = random.randrange(1, 10)
        self.image.fill(self.color) ## This makes it not have shadow
        self.planets.draw(self.image)
        self.stars.draw(self.image) ## This makes it draw over the background
        self.planet_timer -= 1
        self.star_timer -= 1


class BG2(pygame.sprite.Sprite):
    def __init__(self):
        super(BG2, self).__init__()
        self.image = pygame.Surface(c.display_size)
        self.color = (0, 0, 0)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.stars = pygame.sprite.Group()
        self.planets = pygame.sprite.Group()
        self.star_timer = random.randrange(1, 10)
        self.random_timer_range_low = 120
        self.random_timer_range_high = 360
        self.planet_timer = random.randrange(self.random_timer_range_low, self.random_timer_range_high)
        self.max_planets = 1
        self.current_num_planets = 0


    def update(self):
        self.planets.update()
        for planet in self.planets:
            if planet.rect.y > c.display_height:
                self.planets.remove(planet)
                self.current_num_planets -= 1
                print(self.current_num_planets)
                self.planet_timer = random.randrange(self.random_timer_range_low, self.random_timer_range_high)
        if self.planet_timer == 0:
            if self.current_num_planets <= self.max_planets:
                new_planet = Planet()
                self.planets.add(new_planet)
                self.current_num_planets += 1
                self.planet_timer = random.randrange(self.random_timer_range_low, self.random_timer_range_high)
                print(self.planet_timer)
                print(self.current_num_planets)

        self.stars.update()
        for star in self.stars:
            if star.rect.y >= c.display_height:
                self.stars.remove(star)
        if self.star_timer == 0:
            new_star = Star()
            self.stars.add(new_star)
            self.star_timer = random.randrange(1, 10)
        self.image.fill(self.color) ## This makes it not have shadow
        self.planets.draw(self.image)
        self.stars.draw(self.image) ## This makes it draw over the background
        self.planet_timer -= 1
        self.star_timer -= 1


class BG3(pygame.sprite.Sprite):
    def __init__(self):
        super(BG3, self).__init__()
        self.image = pygame.Surface(c.display_size)
        self.color = (0, 150, 50)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.stars = pygame.sprite.Group()
        self.planets = pygame.sprite.Group()
        self.star_timer = random.randrange(1, 10)
        self.random_timer_range_low = 120
        self.random_timer_range_high = 360
        self.planet_timer = random.randrange(self.random_timer_range_low, self.random_timer_range_high)
        self.max_planets = 1
        self.current_num_planets = 0


    def update(self):
        self.planets.update()
        for planet in self.planets:
            if planet.rect.y > c.display_height:
                self.planets.remove(planet)
                self.current_num_planets -= 1
                print(self.current_num_planets)
                self.planet_timer = random.randrange(self.random_timer_range_low, self.random_timer_range_high)
        if self.planet_timer == 0:
            if self.current_num_planets <= self.max_planets:
                new_planet = Planet()
                self.planets.add(new_planet)
                self.current_num_planets += 1
                self.planet_timer = random.randrange(self.random_timer_range_low, self.random_timer_range_high)
                print(self.planet_timer)
                print(self.current_num_planets)

        self.stars.update()
        for star in self.stars:
            if star.rect.y >= c.display_height:
                self.stars.remove(star)
        if self.star_timer == 0:
            new_star = Star()
            self.stars.add(new_star)
            self.star_timer = random.randrange(1, 10)
        self.image.fill(self.color) ## This makes it not have shadow
        self.planets.draw(self.image)
        self.stars.draw(self.image) ## This makes it draw over the background
        self.planet_timer -= 1
        self.star_timer -= 1

class BG4(pygame.sprite.Sprite):
    def __init__(self):
        super(BG4, self).__init__()
        self.image = pygame.Surface(c.display_size)
        self.color = (100, 50, 50)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.stars = pygame.sprite.Group()
        self.planets = pygame.sprite.Group()
        self.star_timer = random.randrange(1, 10)
        self.random_timer_range_low = 120
        self.random_timer_range_high = 360
        self.planet_timer = random.randrange(self.random_timer_range_low, self.random_timer_range_high)
        self.max_planets = 1
        self.current_num_planets = 0

    def update(self):
        self.planets.update()
        for planet in self.planets:
            if planet.rect.y > c.display_height:
                self.planets.remove(planet)
                self.current_num_planets -= 1
                print(self.current_num_planets)
                self.planet_timer = random.randrange(self.random_timer_range_low, self.random_timer_range_high)
        if self.planet_timer == 0:
            if self.current_num_planets <= self.max_planets:
                new_planet = Planet()
                self.planets.add(new_planet)
                self.current_num_planets += 1
                self.planet_timer = random.randrange(self.random_timer_range_low, self.random_timer_range_high)
                print(self.planet_timer)
                print(self.current_num_planets)

        self.stars.update()
        for star in self.stars:
            if star.rect.y >= c.display_height:
                self.stars.remove(star)
        if self.star_timer == 0:
            new_star = Star()
            self.stars.add(new_star)
            self.star_timer = random.randrange(1, 10)
        self.image.fill(self.color)  ## This makes it not have shadow
        self.planets.draw(self.image)
        self.stars.draw(self.image)  ## This makes it draw over the background
        self.planet_timer -= 1
        self.star_timer -= 1