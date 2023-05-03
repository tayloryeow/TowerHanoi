"""
Class file for keeping state, visuals, and control of the problem.

Assumptions for the moment
> Only works for 3 pillars
> Up to 6 discs
"""
import random

# Disc State tracker class
class Disc:
    # Creates a disc of a specified size
    def __init__(self, size):
        self.size = size

    def get_size(self):
        return self.size


# Collection of Discs called a Pillar Class
class Pillar:
    # Creates a pillar in a certain peg location.
    def __init__(self, peg_position, list_of_disc_sizes):
        # Store where the pillar is located
        self.peg_position = peg_position

        # Create a storage list for Discs
        self.discs = []

        # Fill the disc storage list with new Discs
        for disc_size in list_of_disc_sizes:
            self.discs.append(Disc(disc_size))

    # Get a list of disc sizes as ints
    def get_discs(self):
        integer_disc_list = []
        for disc in self.discs:
            integer_disc_list.append(disc.get_size())
        return integer_disc_list

    def is_valid(self):
        last_disc = 0
        for disc in self.discs:
            if last_disc > disc.get_size():
                return False
        return True


'''
Game class. 
Holds the entire game logics, moves, state, and view.
Only touchable classes will be the movement, checking victory, and setup stuff.
'''


class TowersOfHanoi:
    # Initialize a random towers of hanoi problem.
    # - Checks the number of discs given is valid for the num pillars.
    def __init__(self, num_pillars, num_discs):
        # Keep game state descriptors.
        self.num_pillars = num_pillars
        self.num_discs = num_discs

        # Store a reference to all the game state classes. Just a list of pillars really.
        pillars_list = []
        self.game_state = {'pillars': pillars_list}

        #Create a pool of discs to randomly assign to the pillars
        discs_to_assign = range(0, num_discs)
        discs_to_assign = random.shuffle(discs_to_assign)


        # Create the given number of pillars
        for curr_pillar_number in range(0, num_pillars):

            # Manipulate the parameters for the Pillar construction
            disc_list = [1, 2, 3]
            newly_created_pillar = Pillar(curr_pillar_number, disc_list)

            #Add the newly constructed pillar with its discs
            self.game_state['pillars'].append(newly_created_pillar)

    # Textual repr of the game state
    def __str__(self):
        # Loop through each pillar and output them vertically.
        # I.e. pillar 0 is displayed above pillar 1 etc
        pass

    def get_all_discs(self):
        # Holder for all the discs
        # 2d list representation
        disc_reprs = []

        # Get and add each pillar disc reprs to disc holder
        for pillar_index in range(0, self.num_pillars):
            # get a list of discs
            pillars_discs = self.get_pillar(pillar_index).get_discs()
            disc_reprs.append(pillars_discs)
        return disc_reprs

    # Get a specific pillar
    def get_pillar(self, pillar_index):
        return self.game_state['pillars'][pillar_index]
