import unittest

from simulation import Game

"""
- Monty Hall presents 3 doors. OK
- One door must have a car, all others must have a goat.
- Competitor chooses one door. OK
- Monty Hall reveals one of the doors. OK
- The revealed door must not be the chosen door. OK
- Also the revealed door must not have the car. OK
- Competitor may keep or change the door. OK
- S/he can't choose the revealed door (obvious). OK
- If the door contains the goat the competitor looses, if there's a car the competitor wins. OK
"""


class TestSimulationMethods(unittest.TestCase):

    def test_present_doors(self):
        simulation = Game()
        simulation.play()

        doors = simulation.doors
        self.assertEqual(3, len(doors))
        self.assertEqual(1, doors.count(Game.CAR))
        self.assertEqual(2, doors.count(Game.GOAT))

        valid_doors = list(range(0, len(doors)))

        for _ in range(0, 10):
            self.assertIn(simulation.chosen_door, valid_doors)

            revealed = simulation.revealed_door
            self.assertIn(revealed, valid_doors)
            self.assertNotEqual(simulation.chosen_door, revealed)
            self.assertNotEqual(Game.CAR, doors[revealed])

            for _ in range(0, 5):
                past_choice = simulation.chosen_door
                simulation.change_door()
                new_choice = simulation.chosen_door
                self.assertNotEqual(past_choice, simulation.chosen_door)
                self.assertNotEqual(simulation.chosen_door, revealed)
                self.assertIn(new_choice, valid_doors)

    def test_victory_count(self):
        simulation = Game()
        simulation.play()
        simulation.chosen_door = simulation.winning_door
        self.assertEqual(True, simulation.winner())

        simulation = Game()
        simulation.play()
        simulation.chosen_door = simulation.winning_door + 1
        self.assertEqual(False, simulation.winner())


if __name__ == '__main__':
    unittest.main()
