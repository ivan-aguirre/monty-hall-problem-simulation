import argparse
import random
from itertools import starmap


class Game:
    CAR = 1
    GOAT = 0

    def __init__(self):
        self.doors = None
        self.winning_door = None
        self.chosen_door = None
        self.revealed_door = None

    @staticmethod
    def _present_doors():
        doors = [Game.GOAT, Game.GOAT, Game.GOAT]
        doors[random.choice(range(0, len(doors)))] = Game.CAR
        return doors

    def _chose_door(self):
        valid_doors = range(0, len(self.doors))
        return random.choice(valid_doors)

    def _possible_choices(self, enum_criteria):
        return list(starmap(lambda door_position, door_content: door_position,
                            filter(enum_criteria, enumerate(self.doors))))

    def _reveal_door(self):
        possible_choices = self._possible_choices(lambda t: t[0] != self.chosen_door and t[1] != Game.CAR)
        return random.choice(possible_choices)

    def change_door(self):
        possible_doors_enum = self._possible_choices(lambda t: t[0] != self.chosen_door and t[0] != self.revealed_door)
        self.chosen_door = random.choice(possible_doors_enum)

    def play(self):
        self.doors = self._present_doors()
        self.winning_door = self.doors.index(Game.CAR)
        self.chosen_door = self._chose_door()
        self.revealed_door = self._reveal_door()

    def winner(self):
        return self.chosen_door == self.winning_door


def _simulate(n_simulations, change):
    wins = 0
    for _ in range(0, n_simulations):
        game = Game()
        game.play()
        if change:
            game.change_door()
        if game.winner():
            wins += 1
    print(f"Simulations: {n_simulations}")
    print(f"Wins.......: {wins} ({100 * wins / n_simulations}%)")
    print(f"Losses.....: {n_simulations - wins} ({100 * (1 - (wins / n_simulations))}%)")


def simulate(n_simulations):
    print("Simulation without changing the chosen door")
    _simulate(n_simulations, change=False)
    print("")
    print("Simulation changing the chosen door")
    _simulate(n_simulations, change=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("n_simulations", help="number of simulations", type=int)
    args = parser.parse_args()
    simulate(int(args.n_simulations))
