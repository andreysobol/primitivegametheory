players = ("player1", "player2")

strategies = ("cheat", "cooperate")

player1_strategies = strategies
player2_strategies = strategies

from itertools import product

multiplied_strategies = product(player1_strategies, player2_strategies)
