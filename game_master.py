from strategies. random_strategies import random_simple
from strategies. methodical import fill_left_right
from game.run_game import run_game


# Run the game using the following parameters:
#   - Player 1 name "Random" and Player 2 name "Left-Right".
#   - Player 1 will use the random "random_simple" strategy while player two will use the methodical "fill_left_right" strategy
#   - Will proceed to the next move when Enter is pressed
#   - Will timeout if a move takes more than 1 second
run_game("Random", "Left-Right", random_simple, fill_left_right, move_duration=-1, max_move_time=1)
