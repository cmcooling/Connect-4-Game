import random
from New_strats import open_lane_check

def check_column(board,player_number):
    '''Checks the board for a vertical 3 in a row'''
    keylanes=[]
    playernos=[1,2]
    playernos.remove(player_number)
    opponent_number = playernos[0]
    
    for column in range(7):
        for i_start in range(3):
            start_owner = board[column][i_start]

            if start_owner == 0:
                continue
                        
            elif start_owner != player_number:
                continue
                             
            elif board[column][i_start+3] == opponent_number:
                continue
            
            for i_next in range(i_start, i_start + 3):
                if board[column][i_next] != start_owner:
                        break
            
            else:
                keylanes.append(column)
    return keylanes

def blocking_vertical(board,player_number):
    lanes=open_lane_check.check(board)
    playernos=[1,2]
    playernos.remove(player_number)
    opponent_number=playernos[0]
    
    block = check_column(board,opponent_number)
    block = [x for x in block if x in lanes]
    
    if len(block)!=0:
        return random.choice(block)        
    else:
        return []

def winning_vertical(board,player_number):
    lanes=open_lane_check.check(board)
    
    win = check_column(board,player_number)
    win = [x for x in win if x in lanes]
    
    if len(win)!=0:
        return random.choice(win)          
    else:
        return []
    
def vertical_strat(board,player_number):
    lanes=open_lane_check.check(board)
    win=winning_vertical(board,player_number)
    block=blocking_vertical(board,player_number)
    if type(win)==int :
        print('using win v')
        return win
    elif type(block)==int:
        print('using block v')
        return block
    else:
        return random.choice(lanes)

        
#%%
board=[[1,2,2,2,1,2],[1,2,1,2,2,2],[1,2,2,2,1,2],[1,2,1,2,1,2],[1,2,1,2,1,2],[1,1,1,2,0,0],[1,2,2,2,1,0]]
#winning_vertical(board,1)
vertical_strat(board,1)