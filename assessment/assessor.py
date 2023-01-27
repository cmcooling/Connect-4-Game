from game.run_game import run_game
from strategies import random_strategies
import random
from joblib import Parallel, delayed
import multiprocessing


def random_opponent(board, player_number):
    return(random.choice(tuple(i_col for i_col, col in enumerate(board) if not min(col))))


def play_matches(n_match, student_strategy):
    results = {"wins": 0, "draws": 0, "losses": 0, "forfeits": 0}

    for i_match in range(n_match):
        result = run_game("Student", "Opponent", student_strategy, random_opponent, print_output=False, max_move_time=1, randomise_first_player=True)

        if result[0] == 1:
            results["wins"] += 1
        elif result[0] == 0:
            results["draws"] += 1
        elif result[1]:
            results["forfeits"] += 1
        else:
            results["losses"] += 1

    return(results)


def assess(student_strategy):
    n_match = 1000
    n_core = multiprocessing.cpu_count()
    n_match_per_core = max(n_match // n_core, 1)
    n_match = n_core * n_match_per_core

    # Ask for a tally from each core
    # Ask each core to sample n/n_core points so n points will be sampled in total
    thread_results = Parallel(n_jobs=n_core)(delayed(play_matches)(n_match_per_core, student_strategy) for i in range(n_core))

    results = {"wins": 0, "draws": 0, "losses": 0, "forfeits": 0}

    for thread_result in thread_results:
        for key, value in thread_result.items():
            results[key] += value

    mark = 0.25 * (n_match - results["forfeits"]) / n_match + 0.75 * ((results["wins"] + 0.5 * results["draws"]) / n_match) ** 3

    print("Results\nWins: {}\nDraws: {}\nLosses: {}\nForfeits: {}\nMark: {}%".format(results["wins"], results["draws"], results["losses"], results["forfeits"], round(mark * 100, 2)))


if __name__ == "__main__":
    assess(random_strategies.simple)
