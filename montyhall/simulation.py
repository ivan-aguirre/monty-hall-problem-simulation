import argparse
import random


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
        doors[random.randint(0, len(doors) - 1)] = Game.CAR
        return doors

    def _chose_door(self):
        valid_doors = range(0, len(self.doors))
        return random.choice(valid_doors)

    def _reveal_door(self):
        def remaining_doors(index_value_tuple):
            door_num, door_value = index_value_tuple
            return door_num != self.chosen_door and door_value != Game.CAR

        # we could simplify this code assuming that len(self.doors) is always 3...
        possible_choices = list(map(lambda t: t[0], filter(remaining_doors, enumerate(self.doors))))

        return random.choice(possible_choices)

    def change_door(self):
        # we could simplify this code assuming that len(self.doors) is always 3...
        valid_doors = range(0, len(self.doors))
        x = [door_num for door_num in valid_doors if door_num not in (self.chosen_door, self.revealed_door)]
        self.chosen_door = random.choice(x)

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
