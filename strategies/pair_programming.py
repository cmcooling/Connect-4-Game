# This file is designed to be edited during a pair programming exercise in-class
# Beginning with a naive random algorithm, your goal is to improve the strategy
# There are sugested steps you might want to take. Begin with "STEP 1", the  proceed to "STEP 2" and so on (follow the step numbers, not the order they appear in the code)
# You can chose to take other steps if you like
# game_master.py is set up to play your code against a naive random strategy
# Run game_master.py to test how your code does

import random
import copy


def pair(board, player_number):
    # STEP 2: Let's look one move ahead. If there's a move we can take that will make us win we want to take it
    # Loop over the different indices you might chose to consider whether it results in a victory

        # STEP 3: This should be inside the loop
        # Let's see if any of the available columns we might chose will cause us to win
        # First, create a copy of the original board using board_copy = copy.deepcopy(board)
        # We can edit board_copy without altering the original baord variable

        # STEP 4: This should be inside the for loop
        # Use the add_token function from run_game to add one of your tokens to the currently selected row
        # Use the check_victory function from victory_check to see if this new board state results in a victory for you
        # If it does, return the index of the currently considered column
    
    # STEP 5: If the loop above doesn't return a value the strategy will return a random variable
    # The next step you take could be to consider if there are are any columns your opponent could go in to win and go there instead of them
    # Have a go at implenting this yourselves, or taker another step you think would be helpful

    return(random.randint(0, 6))

    # STEP 1: currently this algorithm will place in any column, regardless of it's full or not
    # Modify this function so it will only return a value relating to a non-full column


