import random


class robot:
    name = "machine"
    game = ["pedra", "paper", "tisores"]

    def playing(self):
        choice = random.choice(self.game)
        return choice
class moneda:
    name = "moneda"
    game = ["cara", "creu"]

    def playing(self):
        choice = random.choice(self.game)
        return choice