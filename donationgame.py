players = ("player1", "player2")

strategies = ("cooperate", "cheat")

player1_strategies = strategies
player2_strategies = strategies

from itertools import product

multiplied_strategies = list(product(player1_strategies, player2_strategies))

def calculate_payoffs(multiplied_strategies):
    r = {}
    for strategies in multiplied_strategies:
        if strategies == ("cooperate", "cooperate"):
            payoff = {"player1":2, "player2":2}
        if strategies == ("cooperate", "cheat"):
            payoff = {"player1":-1, "player2":3}
        if strategies == ("cheat", "cooperate"):
            payoff = {"player1":3, "player2":-1}
        if strategies == ("cheat", "cheat"):
            payoff = {"player1":0, "player2":0}
        r[strategies] = payoff
    return r

payoffs = calculate_payoffs(multiplied_strategies)
