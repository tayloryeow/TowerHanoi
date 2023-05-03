import unittest
import towers_of_hanoi


class CreationTest(unittest.TestCase):
    def test_disc_creator(self):
        pass

    '''
    Test that the game state was created correctly.
    > No pillars have impossible disc states
    '''

    def test_constructor(self):
        # Create a tower of Hanoi repr
        towers = towers_of_hanoi.TowersOfHanoi(3, 3)

        # Check that 3 pillars were created
        assert (towers.num_pillars, 3)
        assert (towers.game_state['pillars'], 3)

        # Check that each pillar has a valid configuration of discs

        # Check that discs were created adequately.

if __name__ == '__main__':
    unittest.main()