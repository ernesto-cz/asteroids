from circleshape import CircleShape
import pygame
import random
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        forward = self.velocity * dt
        self.position += forward

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        p_random_angle = self.velocity.rotate(angle)
        n_random_angle = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        icarus = Asteroid(self.position.x, self.position.y, new_radius)
        hallas = Asteroid(self.position.x, self.position.y, new_radius)
        icarus.velocity = p_random_angle * 1.2
        hallas.velocity = n_random_angle * 1.2
