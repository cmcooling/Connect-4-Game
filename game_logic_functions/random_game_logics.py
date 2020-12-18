import random


def random_simple(board, player_number):
    '''A sample turn logic which will take turns randomly with no regard to board state
    (param) board ([[int]*6]*7): The board te move will be taken on
    (param) player_number The number of the player'''

    return(random.randint(0, 6))
