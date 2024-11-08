import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2()

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return #small asteroid
        else:
            random_angle = random.uniform(20, 50)
            asteroid_vector1 = self.velocity.rotate(random_angle)
            asteroid_vector2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_one.velocity = asteroid_vector1 * 1.2
            asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_two.velocity = asteroid_vector2