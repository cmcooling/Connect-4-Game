from run_game import run_game
from game_logic_functions import random_game_logics

run_game("Alice", "Bob", random_game_logics.random_simple, random_game_logics.random_simple, move_duration=1)
