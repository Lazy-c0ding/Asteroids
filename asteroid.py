from circleshape import *
import pygame
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.position.x, self.position.y), self.radius,  2)
    def update(self, dt):
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            new_velocity_1 = self.velocity.rotate(random_angle) * 1.2
            new_velocity_2 = self.velocity.rotate(-random_angle) * 1.2
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_1.velocity = new_velocity_1
            asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_2.velocity = new_velocity_2
            for group in self.groups():
                group.add(asteroid_1)
                group.add(asteroid_2)
