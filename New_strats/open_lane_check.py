def check(board):
    lanes=list(range(7))
    for column in range(7):
        if min(board[column]) != 0:
            lanes.remove(column)
    return lanes