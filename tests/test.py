import random
import unittest


"""
- Monty Hall presents 3 doors. OK
- Competitor chooses one door. OK
- Monty Hall reveals one of the doors, other than the chosen door, that have a goat.
- Competitor may keep or change the door.
- S/he can't choose the revealed door (obvious).
- If the door contains the goat the competitor looses, if there's a car the competitor wins.
- N games can be played.
- The simulation must keep the numbers of wins and loses.
- At the end of simulation the stats must be displayed:
    # Plays
    # Win
    # Loses
  And the respective % 
"""


def present_doors():
    return [0, 0, 0]


def choose_door(valid_doors):
    return random.choice(valid_doors)

def reveal_door():
    return 1


class TestStringMethods(unittest.TestCase):

    def test_present_doors(self):
        doors = present_doors()
        self.assertEquals(3, len(doors))

        valid_doors = list(range(0, len(doors)))

        choice = choose_door(valid_doors)
        self.assertIn(choice, valid_doors)

        revealed = reveal_door()
        self.assertIn(revealed, valid_doors)
        self.assertNotEqual(choice, revealed)


if __name__ == '__main__':
    unittest.main()
