import pygame
from constants import *
from player import Player



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
    Player.containers = updatable, drawable # Set the containers for the Player class

    # Create the player
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))  # Clear the screen with black
        updatable.update(dt)
        for obj in drawable:  # Draw the player
            obj.draw(screen)

        pygame.display.flip()  # Update the display
        fps_clock.tick(60)  # Cap the frame rate at 60 FPS
        dt = fps_clock.get_time() / 1000.0  # delta time / convert milliseconds to seconds
        print(f"Delta time: {dt:.3f} seconds")
if __name__ == "__main__":
    main()
