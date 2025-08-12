import pygame
from asteroid import Asteroid
from player import Player
from shot import Shot
from asteroidfield import AsteroidField
from constants import *

def main():

    # Initialize Pygame
    pygame.init()
    fps_clock = pygame.time.Clock()
    dt = 0.0

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = updatable, drawable  # Set the containers for the Player class
    Asteroid.containers = updatable, drawable, asteroids  # Set the containers for the Asteroid class
    AsteroidField.containers = updatable  # Set the containers for the AsteroidField class
    Shot.containers = updatable, drawable, shots  # Set the containers for the Shot class

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)  # Create the player
    asteroid_field = AsteroidField()  # Create the asteroid field

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))  # Clear the screen with black
        updatable.update(dt)
        asteroid_field.update(dt)
        for asteroid in asteroids:  # Check collisions with asteroids
            if player.collide(asteroid):
                print("Game Over!")
                return
            
        for shot in shots:  # Check collisions with shots
            for asteroid in asteroids:
                if  not shot.collide(asteroid):
                    continue
                shot.kill()
                asteroid.split()
                print("Asteroid hit!")
        for obj in drawable:  # Draw the player
            obj.draw(screen)

        pygame.display.flip()  # Update the display
        fps_clock.tick(60)  # Cap the frame rate at 60 FPS
        dt = fps_clock.get_time() / 1000.0  # delta time / convert milliseconds to seconds
if __name__ == "__main__":
    main()
