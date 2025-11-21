import random


class robot:
    name = "machine"
    game = ["pedra", "paper", "tisores"]

    def playing(self):
        choice = random.choice(self.game)
        return choice
