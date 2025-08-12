import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        rand_angle = random.uniform(20, 50)  # Random angle for the new asteroids
        new_velocity1 = self.velocity.rotate(rand_angle) * 1.2
        new_velocity2 = self.velocity.rotate(-rand_angle) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = new_velocity1
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = new_velocity2
        return asteroid1, asteroid2
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255),self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt