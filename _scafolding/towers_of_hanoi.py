'''
Class file for keeping state, visuals, and control of the problem.

Assumptions for the moment
> Only works for 3 pillars
> Up to 6 discs
'''

class Disc:
    #Creates a disc of a specified size
    def __init__(self, size):
        self.size = size

class Pillar:
    #Creates a pillar in a certain peg location.
    def __init__(self, peg_position, list_of_disc_sizes):
        #Store where the pillar is located
        self.peg_position = peg_position

        #Create a storage list for Discs
        self.discs = []

        #Fill the disc storage list with new Discs
        for disc_size in list_of_disc_sizes:
            self.discs.append(Disc(disc_size))


'''
Game class. 
Holds the entire game logics, moves, state, and view.
Only touchable classes will be the movement, checking victory, and setup stuff.
'''
class TowersOfHanoi:
    # Initialize a random towers of hanoi problem.
    # - Checks the number of discs given is valid for the num pillars.
    def __init__(self, num_pillars = 3, num_discs = 3):
        # Store a reference to all the game state classes. Just a list of pillars really.
        self.game_state = []

        #Create the given of pillars
        for curr_pillar_number in range (0, num_pillars):
            #Manipulate the parameters for the Pillar construction
            disc_list = [1, 2, 3]
            newly_created_pillar = Pillar(curr_pillar_number, disc_list)
            self.game_state.append(newly_created_pillar)

            #generate a list of discs
            #Randomize said discs
            #Feed into pillar


def main():
    #Create a random towers of Hanoi
    towers = TowersOfHanoi()

    #Visualize it
    towers.visualize()

if __name__=="__main__":
    main()
