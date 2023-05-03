import unittest
import numpy as np

import towers_of_hanoi


class CreationTest(unittest.TestCase):
    '''
    Test simple getters stuff for disc
    '''
    def test_disc_creator(self):

        for i in range(0, 6):
            disc = towers_of_hanoi.Disc(i)
            assert(disc.get_size() == i)

    '''
    Test that the game state was created correctly.
    > No pillars have impossible disc states
    '''

    def test_towers_constructor(self):
        # Create a tower of Hanoi repr
        towers = towers_of_hanoi.TowersOfHanoi(3, 3)

        # Check that 3 pillars were created
        assert (towers.num_pillars == 3)
        assert (len(towers.game_state['pillars']) == 3)

        # Check that each pillar has a valid configuration of discs
        for i in range(0, 3):
            pillar = towers.get_pillar(i)
            assert(pillar.is_valid())

        # Check that each disc is unique across all pillars
        disc_list = towers.get_all_discs()
        disc_list = list(np.concatenate(disc_list).flat)

        disc_set = set(disc_list)
        assert (len(disc_set) == len(disc_list))


if __name__ == '__main__':
    unittest.main()
