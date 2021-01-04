from run_game import run_game
from game_logic_functions import random_strategies
from game_logic_functions import methodical

run_game("Left", "Random", methodical.fill_left_right, random_strategies.random_simple, move_duration=1, max_move_time=1)
