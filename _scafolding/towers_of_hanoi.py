'''
Class file for keeping state, visuals, and control of the problem.

Assumptions for the moment
> Only works for 3 pillars
> Up to 6 discs
'''

# Disc State tracker class
class Disc:
    # Creates a disc of a specified size
    def __init__(self, size):
        self.size = size


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

    def get_dics(self):
        return self.discs


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

        # Create the given number of pillars
        for curr_pillar_number in range(0, num_pillars):
            # Manipulate the parameters for the Pillar construction
            disc_list = [1, 2, 3]
            newly_created_pillar = Pillar(curr_pillar_number, disc_list)
            self.game_state['pillars'].append(newly_created_pillar)

            # generate a list of discs
            # Randomize said discs
            # Feed into pillar

    # Textual repr of the game state
    def __str__(self):
        # Loop through each pillar and output them vertically.
        # I.e. pillar 0 is displayed above pillar 1 etc
        pass

    # Get a specific pillar
    def get_pillar(self, pillar_index):
        return self.game_state['pillars'][pillar_index]

