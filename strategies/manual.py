def manual(board, player_number):
    '''This will ask for the person running the game to input the move as an integer before each turn.
    Enter a number from 0 to 6 and press enter to move.
    (param) board ([[int]*6]*7): The board te move will be taken on
    (param) player_number The number of the player'''
    i = int(input("Input a move: "))
    return(i)
