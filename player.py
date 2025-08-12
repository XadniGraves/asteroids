import pygame
from shot import Shot
from circleshape import CircleShape
from constants import *



class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0 # in degrees
        self.shot_cooldown = 0  # to track the last time the player shot

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

    def shoot(self):
        # Create a shot at the front of the player
        shot_position = self.position + pygame.Vector2(0, 1).rotate(self.rotation) * self.radius
        shot = Shot(shot_position.x, shot_position.y, SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0, SHOT_SPEED).rotate(self.rotation)

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

        if self.shot_cooldown > 0:
            self.shot_cooldown -= dt

        if keys[pygame.K_SPACE] or keys[pygame.mouse.get_pressed()[0]]:
            if self.shot_cooldown <= 0:
                self.shoot()
                self.shot_cooldown = SHOT_COOL_DOWN

        print(f"Shot cooldown: {self.shot_cooldown:.2f} seconds")
