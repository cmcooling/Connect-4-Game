from strategies import methodical, random_strategies, manual

# from strategies import a_min_max  # a_min_max.pick_best_move - Amin Akhtar
# from strategies import winning_strat_Joshua  # winning_strat_Joshua.winning - Joshua Cho
# from strategies import vertex1  # vertex1.vertex - Varja Cuculovic
# from strategies import chao_fan_dumb_strategy  # chao_fan_dumb_strategy.smart - Chao Fan
# from strategies import KaFanConnect4Code  # KaFanConnect4Code.Kf2 - Ka Fan
# from strategies import logan_strategy  # logan_strategy.strategy - Logan Filipovich
# from strategies import jgstrat  # jgstrat.from_middle - Jaidip Gill
# from strategies import Kaiyu_Hu  # Kaiyu_Hu.dumb - Kaiyu Hu
# from New_strats import New_strat  # New_strat.Strat - Zhen Liew
# from strategies import easy_strategy  # easy_strategy.my_strategy - Mingze Ma         ***REQUIRES NUMPY INSTALLED***
# from strategies import connect4_strategy  # connect4_strategy.second_strategy - David Noyvert
# from strategies import mystrat  # mystrat.beginner_strat - Minjoon Seo
from strategies import sterge_tactic_variable_depth  # sterge_tactic_variable_depth.sterge - Stergios Vlachopoulos
# from strategies import strats  # strat.strat - Lok Lau

from strategies import samantha


from run_game import run_game


# Run the game using the following parameters:
#   - Player 1 name "Left" and Player 2 name "Random".
#   - Player 1 will use the methodical "fill_left_right" strategy while player two will use a random strategy
#   - Pause 1 second between moves and timeout if a move takes more than 1 second
# run_game("Sam", "Random", samantha.sam, random_strategies.random_simple, move_duration=-1, max_move_time=1)
run_game("Sam", "Sterge", samantha.sam, sterge_tactic_variable_depth.sterge, move_duration=-1, max_move_time=1)
