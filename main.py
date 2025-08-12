import pygame
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

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))  # Clear the screen with black

    pygame.display.flip()  # Update the display
    fps_clock.tick(60)  # Cap the frame rate at 60 FPS
    dt += fps_clock.get_time() / 1000.0 # delta time / convert milliseconds to seconds
    
if __name__ == "__main__":
    main()
