# Testing different GUI application

# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([1280, 720])

# Fill the background with white
screen.fill((255, 255, 255))

# Run superloop until the running variable is quit
start_running = True
while start_running:
    # Has that button been pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start_running = False

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # Update the full display Surface to the screen
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()