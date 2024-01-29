from game.run_game import run_game
from strategies import random_strategies
import random


def random_opponent(board, player_number):
    return(random.choice(tuple(i_col for i_col, col in enumerate(board) if not min(col))))


def calculate_mark(wins, draws, forfeits, n_match):
    return 0.25 * (n_match - forfeits) / n_match + 0.75 * ((wins + 0.5 * draws) / n_match) ** 3


def assess(student_strategy):
    n_match = 1000

    wins = 0
    draws = 0
    losses = 0
    forfeits = 0

    for i_match in range(n_match):
        print("Beginning game {} of {}.".format(i_match + 1, n_match), end="\r")

        result = run_game("Student", "Opponent", student_strategy, random_opponent, print_output=False, max_move_time=1, randomise_first_player=True)

        if result[0] == 1:
            wins += 1
        elif result[0] == 0:
            draws += 1
        elif result[1]:
            forfeits += 1
        else:
            losses += 1

    print(" " * 100)

    mark = calculate_mark(wins, draws, forfeits, n_match)

    print("Results\nWins: {}\nDraws: {}\nLosses: {}\nForfeits: {}\nMark: {}%".format(wins, draws, losses, forfeits, round(mark * 100, 2)))


if __name__ == "__main__":
    assess(random_strategies.simple)
