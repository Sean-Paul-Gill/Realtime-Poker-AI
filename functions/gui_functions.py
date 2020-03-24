import pygame
import sys

# Setting screen variables
screen_width, screen_height = 1280, 720

# Importing Colours
WHITE = (255, 255, 255)
TURQOISE = (47, 132, 155)

"""
button_check:
 - `pos` is the `x,y` from `event.pos`
 - x, y is the x/y co-ords from the x/y where you render a button
 - x1, y1 is the width/height for the button.
 - This function will return true if the button is clicked on.
"""
def button_check(pos, x, y, x1, y1):
    return pos[0] >= x and pos[0] < x + x1 and pos[1] >= y and pos[1] < y + y1


"""
make_button:
 - `surface` is like the default 'DISPLAYSURF', `color` is the color of the box
 - `text_color` is the color of the text in the box
 - `x/y` are the co-ords of the button. `width/height` are the dimensions of button
 - `text` is the text for the label.
"""
def make_button(surface, color, text_color, x, y, width, height, text):
    pygame.draw.rect(surface, (0,0,0),(x-1,y-1,width+2,height+2),1) #makes outline around the box
    pygame.draw.rect(surface, color,(x,y,width,height))     #mkes the box

    myfont = pygame.font.SysFont('Arial Black', 30)  #creates the font
    label = myfont.render(text, 1, text_color) #creates the label
    surface.blit(label, (x+2, y)) #renders the label

# The Starting Screen
def starting_screen():
    # Testing different GUI application
    pygame.init()

    # Set up the drawing window
    screen = pygame.display.set_mode([screen_width, screen_height])

    # Fill the background with white
    screen.fill(WHITE)

    # Blit the Start-menu Back-ground on
    background_image = pygame.image.load("start_screen.png").convert()
    screen.blit(background_image, [0,0])

    # Initializing Buttons on Screen
    menu_counter, menu_items = 0, ['2 Players', '3 Players', '4 Players', 'Help', 'Quit']
    button_width, button_height = 180, 60
    button_pos_x, button_pos_y = 540, 220
    for menu_item in menu_items:
        make_button(screen, TURQOISE, WHITE, button_pos_x, button_pos_y + (menu_counter*80), button_width, button_height, menu_item)
        menu_counter = menu_counter+1

    # Run superloop until the running variable is quit
    start_running = True
    while start_running:
        # Capture all the events on the screen
        for event in pygame.event.get():
            # The close button
            if event.type == pygame.QUIT:
                start_running = False

            #Check if buttons have been 2 players has been pressed
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                # Check if any of the buttons were pressed
                menu_counter = 0
                for menu_item in menu_items:
                    if button_check(pygame.mouse.get_pos(), button_pos_x, button_pos_y+(80*menu_counter), button_width, button_height):
                        if (menu_item == '3 Players') or (menu_item == 'Quit'):
                            game_type = menu_item
                            start_running = False
                        else:
                            print(menu_item+" is currently under development...")
                            break
                    menu_counter = menu_counter+1

        # Update the full display Surface to the screen
        pygame.display.flip()

    # Quitting the start-up
    pygame.quit()

    # Returning how many players to display
    return game_type

# The Gameplay GUI
def gameplay_screen():
    # Testing different GUI application
    pygame.init()

    # Set up the drawing window
    screen = pygame.display.set_mode([screen_width, screen_height])

    # Fill the background with white
    screen.fill(WHITE)

    # Blit the Start-menu Back-ground on
    background_image = pygame.image.load("gameplay_layer.png").convert()
    screen.blit(background_image, [0, 0])

    start_running = True
    while start_running:
        # Capture all the events on the screen
        for event in pygame.event.get():
            # The close button
            if event.type == pygame.QUIT:
                start_running = False

        # Update the full display Surface to the screen
        pygame.display.flip()

    # Quitting the start-up
    pygame.quit()