This folder ("New_strats") is a self contained algorithm. As long as this folder is put into the main folder
("Connect-4-Game-master") it will work when imported.

The only module that will need to be imported is New_strats.py.
The function that will call the algorithm is New_strats.Strat(board, player_number).

EXAMPLE CODE (to input into "game_master.py"):

"""
from New_strats import New_strat

run_game("New_strat", "example_tactic", New_strat.Strat, example_tactic, move_duration=1, max_move_time=1)
"""
