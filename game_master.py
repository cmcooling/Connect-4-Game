from run_game import run_game
from game_logic_functions import random_game_logics
from game_logic_functions import methodical

run_game("Left", "Random", methodical.fill_left_right, random_game_logics.random_simple, move_duration=1)
