from run_game import run_game
from strategies import random_strategies
import random


def random_opponent(board, player_number):
    return(random.choice(tuple(i_col for i_col, col in enumerate(board) if not min(col))))


def assess(student_strategy):
    n_match = 1000

    wins = 0
    draws = 0
    losses = 0
    forfeits = 0

    for i_match in range(n_match):
        result = run_game("Student", "Opponent", student_strategy, random_opponent, print_output=False, max_move_time=1, randomise_first_player=True)

        if result[0] == 1:
            wins += 1
        elif result[0] == 0:
            draws += 1
        elif result[1]:
            forfeits += 1
        else:
            losses += 1

    mark = 0.5 * (n_match - forfeits) / n_match + 0.5 * ((wins + 0.5 * draws) / n_match) ** 2

    print("Results\nWins: {}\nLosses: {}\nForfeits: {}\nMark: {}".format(wins, losses, forfeits, mark))


assess(random_strategies.random_simple)