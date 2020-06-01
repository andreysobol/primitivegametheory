players = ("player1", "player2")

strategys = ("cheat", "cooperate")

player1_strategys = strategy
player2_strategys = strategy

from itertools import product

multiplied_strategys = product(player1_strategy, player2_strategys)
