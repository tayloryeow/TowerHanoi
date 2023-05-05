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
    def __init__(self, size, color):
        self.size = size
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
    def __init__(self, num_disks):
        self.num_disks = num_disks
        self.towers = []

        # Create the towers
        tower_width = 10
        tower_height = 400
        tower_x = [size[0] // 4 - tower_width // 2, size[0] // 2 - tower_width // 2,
                   3 * size[0] // 4 - tower_width // 2]
        tower_y = size[1] - tower_height
        tower_colors = [RED, GREEN, BLUE]
        for i in range(3):
            self.towers.append(Tower(tower_x[i], tower_y, tower_colors[i]))

        # Create the disks
        disk_colors = [RED, GREEN, BLUE]
        disk_size = [60, 40, 20]
        disk_x = size[0] // 2
        disk_y = size[1] - tower_height
        for i in range(num_disks):
            self.towers[0].add_disk(Disk(disk_size[i], disk_colors[i]))
            disk_y -= 20

    # Draw the towers and disks
    def draw(self):
        screen.fill(WHITE)

        # Draw the towers
        tower_width = 10
        tower_height = 400
        for tower in self.towers:
            pygame.draw.rect(screen, tower.color, [tower.x, tower.y, tower_width, tower_height])

        # Draw the disks
        disk_y = size[1] - tower_height + 10
        for tower in self.towers:
            disk_x = tower.x - tower.disks[0].size // 2 + tower_width // 2
            for disk in tower.disks:
                disk_height = 20
                pygame.draw.rect(screen, disk.color, [disk_x, disk_y, disk.size, disk_height])
                disk_y -= disk_height

            disk_y = size[1] - tower_height + 10

        pygame.display.flip()

