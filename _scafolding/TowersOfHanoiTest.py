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


if __name__ == '__main__':
    unittest.main()
