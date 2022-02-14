from strategies import random_strategies, pair_programming
from run_game import run_game


# Run the game using the following parameters:
#   - Player 1 name "Left" and Player 2 name "Random".
#   - Player 1 will use the methodical "fill_left_right" strategy while player two will use a random strategy
#   - Pause 1 second between moves and timeout if a move takes more than 1 second
run_game("Pair", "Random", pair_programming.pair, random_strategies.random_simple, move_duration=-1, max_move_time=1)
