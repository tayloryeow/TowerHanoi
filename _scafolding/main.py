import pygame
from towers_of_hanoi import TowerOfHanoi

def main():
    pygame.init()

    # Set the size of the screen
    size = (800, 600)
    screen = pygame.display.set_mode(size)

    # Set the caption of the screen
    pygame.display.set_caption("Tower of Hanoi")

    # Create a Tower of Hanoi game with 6 disks and 3 towers
    toh = TowerOfHanoi(3, 6)

    # Keep the window open until the user closes it
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # Draw the initial state of the game
        toh.draw()

if __name__ == "__main__":
    main()