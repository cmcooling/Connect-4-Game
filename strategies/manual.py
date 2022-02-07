from exceptions import InvalidMoveException


def manual(board, player_number):
    '''This will ask for the person running the game to input the move as an integer before each turn.
    Enter a number from 0 to 6 and press enter to move.
    (param) board ([[int]*6]*7): The board te move will be taken on
    (param) player_number The number of the player'''
    i = input("Input a move: ")
    try:
        i_int = int(i)
    except ValueError:
        raise InvalidMoveException("The value entered could not be converted to an integer")

    if i_int < 0 or i_int > 6:
        raise InvalidMoveException("The index entered must be between 0 and 6")

    return(i_int)
