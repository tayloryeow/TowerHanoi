import pygame
import sys

pygame.init()

'''
DEFINITIONS
'''
# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set the size of the screen
size = (800, 600)
screen = pygame.display.set_mode(size)

# Set the caption of the screen
pygame.display.set_caption("Tower of Hanoi")


# Define the disks
class Disk:
    def __init__(self, width, color):
        self.height = 25
        self.width = width
        self.color = color



# Define the towers
class Tower:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.disks = []

    # Add a disk to the top of the tower
    def add_disk(self, disk):
        self.disks.append(disk)

    # Remove the top disk from the tower and return it
    def remove_disk(self):
        return self.disks.pop()


# Define the Tower of Hanoi game
class TowerOfHanoi:
    def __init__(self, num_towers, num_disks):
        self.num_disks = num_disks  # Number of Disks across all pilllars
        self.towers = []  # Tower list of Tower Objects

        # Create the towers
        tower_width = 10  # Tower width in Pixels
        tower_height = 400  # Tower height in Pixels

        # Base Tower - X Cord location
        tower_x = [size[0] // 4 - tower_width // 2, size[0] // 2 - tower_width // 2,
                   3 * size[0] // 4 - tower_width // 2]

        # Base Tower - Y Cord Location
        tower_y = size[1] - tower_height

        # List of Predefined Colours for the towers

        # Add to this list to
        # extend the number of colours for towers
        tower_colors = [RED, GREEN, BLUE]

        # Create each tower for the game
        for i in range(num_towers):
            # Modulus the colours to make it extensible.
            tower_color = tower_colors[i % len(tower_colors)]
            # Put the tower in the tower list
            self.towers.append(Tower(tower_x[i], tower_y, tower_color))

        # Create the disks
        disk_colors = [RED, GREEN, BLUE]  # Color assignment list
        for i in range(num_disks):
            # Width of disk - Loop starts with the largest disk and works downwards
            disk_size = (num_disks - i) * 20
            disk_color = disk_colors[i % len(disk_colors)]
            # Add all the towers to the very first tower
            self.towers[0].add_disk(Disk(disk_size, disk_color))

    # Draw the towers and disks
    def draw(self):
        screen.fill(WHITE)

        # Draw the towers
        tower_width = 10
        tower_height = 400
        self.draw_towers(tower_width, tower_height)

        # Draw the disks
        self.Draw_discs(tower_width, tower_height)

        pygame.display.flip()

    def Draw_discs(self, tower_width, tower_height):
        num_of_discs_added = 0
        for tower in self.towers:
            for disk in tower.disks:
                # Disk Calculation - X coordinate
                disk_x = (tower.x + tower_width//2)- disk.width//2
                # Disk Calculation - Y coordinate
                disk_y = tower.y + tower_height - (num_of_discs_added * disk.height)

                pygame.draw.rect(screen, disk.color, [disk_x, disk_y, disk.width, disk.height])
                num_of_discs_added += 1

            disk_y = size[1] - tower_height + 10

    def draw_towers(self, tower_width, tower_height):
        for tower in self.towers:
            pygame.draw.rect(screen, tower.color, [tower.x, tower.y, tower_width, tower_height])
