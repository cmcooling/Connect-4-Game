import copy
import random
import time
from game.exceptions import InvalidMoveException, MoveExceptionError

from game.board_printer import print_board
from game.function_timeout import timeout
from game.victory_check import check_victory


def run_game(name_1, name_2, function_1, function_2, print_output=True, move_duration=0, max_move_time=0, randomise_first_player=True):
    '''Runs the game
    (param) name_1 (string): The name of the first player
    (param) name_1 (string): The name of the second player
    (param) function_1 (function): The logic function of the first player
    (param) function_2 (function): The logic function of the second player
    (param) print_output (bool)(optional, default=True): If the output will be printed
    (param) move_duration (float)(optional, default=0): The time the code will pause for each move. If negative, will wait for enter to be pressed
    (param) max_move_time (float)(optional, default=0): The maximum time a move may be considered for in s(0 means it won't be limited)
    (param) randomise_first_player (bool)(optional, default=True): Whether the first player will be randomly chosen
    (return) Will be a tuple with two values. The firs denotes the winner. 0 for no win, 1 for player 1 win, or 2 for player 2 win. The second value will be True if the game ended in a forfeit and False if not.'''
    # Create the board
    board = [[0] * 6 for i in range(7)]

    # Possibly swap the order
    swap_order = random.randint(0, 1) and randomise_first_player

    if swap_order:
        names = [name_2, name_1]
        functions = [function_2, function_1]
        player_numbers = [2, 1]
        player_names = [name_2, name_1]
    else:
        names = [name_1, name_2]
        functions = [function_1, function_2]
        player_numbers = [1, 2]
        player_names = [name_1, name_2]

    if print_output:
        print(names[0] + " will go first")
        print_board(board)
        time.sleep(max(move_duration, 0))

    for i in range(42):
        # Create a new function with the timeout decorator added
        if max_move_time:
            current_logic = timeout(timeout=max_move_time)(functions[i % 2])
        else:
            current_logic = functions[i % 2]

        # Take the current turn
        try:
            victory = process_turn(board, current_logic, player_numbers[i % 2], player_names[i % 2], print_output)
        except InvalidMoveException:
            if print_output:
                print("{} made an invalid move, so {} wins!".format(player_names[i % 2], player_names[(i + 1) % 2]))
            if player_numbers[i % 2] == 1:
                return 2, True
            else:
                return 1, True
        except MoveExceptionError:
            if print_output:
                print("{} returned an error when asked for a move, so {} wins!".format(player_names[i % 2], player_names[(i + 1) % 2]))
            if player_numbers[i % 2] == 1:
                return 2, True
            else:
                return 1, True
        except TimeoutError:
            if print_output:
                print("{} took too long to make a move, so {} wins!".format(player_names[i % 2], player_names[(i + 1) % 2]))
            if player_numbers[i % 2] == 1:
                return 2, True
            else:
                return 1, True

        if print_output:
            print("X {}".format(name_1))
            print("O {}".format(name_2))
            print_board(board)
            print_victory(victory, name_1, name_2)

        if victory:
            return(victory, False)

        if move_duration >= 0:
            time.sleep(move_duration)
        else:
            input("Press Enter to continue...")


def process_turn(board, strategy, player_number, player_name, print_output):
    '''Processes a turn for the specified player
    (param) board ([[int]*6]*7): A board
    (param) strategy (function) The function which returns which column the token is to be added to
    (param) player_number The number of the player'''

    # Copy the board so the original can't be modified
    board_copy = copy.deepcopy(board)

    try:
        # Get the index of the column selected by the move logic
        i_column_add = strategy(board_copy, player_number)
    except TimeoutError:
        raise
    except Exception:
        raise MoveExceptionError("Player {} raised an exception when asked for a move.")

    if print_output:
        print("Player {} selects column {}".format(player_name, i_column_add))

    # Check the value provided is valid
    if type(i_column_add) != int:
        raise InvalidMoveException("The provided column index was {} when it should be an integer".format(i_column_add))

    if i_column_add < 0 or i_column_add > 6:
        raise InvalidMoveException("The provided column index was {} when it should be between 0 and 6, inclusive".format(i_column_add))

    add_token(board, i_column_add, player_number)

    return check_victory(board)


def add_token(board, i_column, player_number):
    '''Adds a token to the specified column of the board
    (param) board ([[int]*6]*7): A board
    (param) i_column (int): The index of the board the token is to be added to
    (param) player_number (int): The number of the player whose token is to be added
    '''

    for i_row in range(6):
        if not board[i_column][i_row]:
            board[i_column][i_row] = player_number
            break
    else:
        raise InvalidMoveException("The provided column index was {}, which corresponded to a full column".format(i_column))


def print_victory(victory, name_1, name_2):
    '''Prints if there's a victory'''
    if victory == 1:
        print(name_1 + " won the game by connecting 4!")
    elif victory == 2:
        print(name_2 + " won the game by connecting 4!")
    elif victory < 0:
        print("The game ended in a draw as the board was full!")
