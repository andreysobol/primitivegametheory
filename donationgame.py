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

def check_nash_equilibrium(multiplied_strategies, payoffs, strategy, players):
    result = True
    payoff = payoffs[strategy]
    for potential_strategy in multiplied_strategies:
        eq = lambda x : x[0] == x[1]
        diff = list(map(eq, zip(strategy, potential_strategy)))
        if diff.count(False) == 1:
            player_index = diff.index(False)
            player = players[player_index]
            player_strategy_payoff = payoff[player]
            potential_player_strategy_payoff = payoffs[potential_strategy][player]
            if potential_player_strategy_payoff > player_strategy_payoff:
                result = False
    return result

assert(False == check_nash_equilibrium(multiplied_strategies, payoffs, ("cooperate", "cooperate"), players))
assert(False == check_nash_equilibrium(multiplied_strategies, payoffs, ("cooperate", "cheat"), players))
assert(False == check_nash_equilibrium(multiplied_strategies, payoffs, ("cheat", "cooperate"), players))
assert(True == check_nash_equilibrium(multiplied_strategies, payoffs, ("cheat", "cheat"), players))

print(False == check_nash_equilibrium(multiplied_strategies, payoffs, ("cooperate", "cooperate"), players))
print(False == check_nash_equilibrium(multiplied_strategies, payoffs, ("cooperate", "cheat"), players))
print(False == check_nash_equilibrium(multiplied_strategies, payoffs, ("cheat", "cooperate"), players))
print(True == check_nash_equilibrium(multiplied_strategies, payoffs, ("cheat", "cheat"), players))