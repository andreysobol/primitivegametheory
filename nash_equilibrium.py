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