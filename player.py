import pygame
from shot import Shot
from circleshape import CircleShape
from constants import *



class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0 # in degrees
        self.last_shot_time = 0  # to track the last time the player shot

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2) # draw the triangle outline

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def can_shoot(self):
        # Check if the player can shoot based on a cooldown
        return pygame.time.get_ticks() - self.last_shot_time > SHOT_COOL_DOWN

    def shoot(self):
        # Create a shot at the front of the player
        shot_position = self.position + pygame.Vector2(0, 1).rotate(self.rotation) * self.radius
        shot = Shot(shot_position.x, shot_position.y, SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0, SHOT_SPEED).rotate(self.rotation)
        self.last_shot_time = pygame.time.get_ticks()

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(-dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_SPACE] or keys[pygame.mouse.get_pressed()[0]]:
            if self.can_shoot():
                self.shoot()
