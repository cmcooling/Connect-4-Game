# A sample solution to the pair programming task

import random
import copy
# Import the functions we need
from run_game import add_token
from victory_check import check_victory


def pair(board, player_number):
    # STEP 2
    # Loop over the values 0-6 inclusive, representing each of the columns
    for index in range(7):
        # STEP 3
        board_copy = copy.deepcopy(board)

        # STEP 4
        # Add our token to the board in the relevant column
        # Note we needed to impoty add_token at the top of the file
        add_token(board_copy, index, player_number)
        # Check for victory with the updated board state
        if check_victory(board_copy) == player_number:
            # If it results in a victory then return the index of the column being considered
            return(index)

        # If it doesn't lead to a victory the loop will move on to consider the next column

    # STEP 5
    # This is simplistic, but we're going to check if there's anywhere the opponent could go to win, and go there instead
    # Get the opponent's number
    if player_number == 1:
        opponent_number = 2
    else:
        opponent_number = 1

    # This code is the same as for step 4, but adding the opponent's number instead
    for index in range(7):
        board_copy = copy.deepcopy(board)

        add_token(board_copy, index, opponent_number)
        print("opponent", index, check_victory(board_copy))
        if check_victory(board_copy) == opponent_number:
            return(index)

    # STEP 1
    # Initially assume the move is invalid. Keeping drawing random numbers until we get one that isn't invalid
    invalid = True
    while invalid:
        # Chose a random index to consider
        index = random.randint(0, 6)
        # If the minimum value in the column is zero, it has empty space, do we can return it
        print("Random: ", index, board[index])
        if min(board[index]) == 0:
            return index
        # If the return statement isn't reached, the column doesn't have space so go back to the top of the loop and chose another column
