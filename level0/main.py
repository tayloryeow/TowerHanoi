import sys
import time

import pygame

from _scafolding.towers_of_hanoi import TowerOfHanoi

"""
WRITE YOUR CODE IN HERE!!!

Alogirthm to solve the towers of hanoi problem

"""
def solve(towers):
    pass


def mouse_in_button_box(button_height, button_width, button_x, button_y, mouse_x, mouse_y):
    return button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height


def main():
    pygame.init()

    # Set the size of the screen
    size = (800, 600)
    screen = pygame.display.set_mode(size)

    # Set the caption of the screen
    pygame.display.set_caption("Tower of Hanoi")

    # Create a Tower of Hanoi game with 6 disks and 3 towers
    toh = TowerOfHanoi(3, 6)

    # Aniomation Defintions
    turn_time = 0.1

    # Define the font for the button text
    font = pygame.font.Font(None, 36)

    # Define the button text and dimensions
    button_text = font.render("Solve", True, (255, 255, 255))
    button_width = 100
    button_height = 50

    # Define button Coordinates
    button_x = 100 - button_width // 2
    button_y = size[1] // 4 - button_height - 10

    # Draw the initial state of the game and the button
    toh.draw()
    pygame.draw.rect(screen, (0, 255, 0), [button_x, button_y, button_width, button_height])
    screen.blit(button_text, (button_x + 10, button_y + 10))

    pygame.display.flip()

    # Keep the window open until the user closes it
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the mouse click was inside the button
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if mouse_in_button_box(button_height, button_width, button_x, button_y, mouse_x, mouse_y):
                    # Solve the Tower of Hanoi problem recursively
                    solve(toh)
            elif event.type == pygame.KEYDOWN:
                # Check for keyboard input to move disks
                if event.key == pygame.K_DOWN:
                    toh.move_disk(0, 1)
                elif event.key == pygame.K_UP:
                    toh.move_disk(0, 2)
                elif event.key == pygame.K_LEFT:
                    toh.move_disk(1, 0)
                elif event.key == pygame.K_RIGHT:
                    toh.move_disk(1, 2)
        toh.draw()





if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
