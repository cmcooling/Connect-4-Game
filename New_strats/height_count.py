def count(board,column):
    empty_spaces=board[column].count(0)
    filled_spaces=6-empty_spaces
    return filled_spaces