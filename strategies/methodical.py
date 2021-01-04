def fill_left_right(board, player_number):
    '''Fills us the left column, then the next leftmost, and so on'''
    for i_column in range(7):
        if min(board[i_column]) == 0:
            return i_column


def fill_right_left(board, player_number):
    '''Fills us the right column, then the next rightmost, and so on'''
    for i_column in range(6, -1, -1):
        if min(board[i_column]) == 0:
            return i_column
