import random
from New_strats import open_lane_check, height_count


def check_row(board,player_number):
    '''Checks for horizontal 3 in a row'''
    keylanes=[]
    dangerlanes=[]
    playernos=[1,2]
    playernos.remove(player_number)
    opponent_number = playernos[0]
    
    for i_row in range(6):
        for i_start in range(0,4):
            start_owner = board[i_start][i_row]
            if start_owner==0:
                continue
            
            elif start_owner!=player_number:
                continue
            
            elif board[i_start+3][i_row]==opponent_number:
                continue
            
            for i_next in range(i_start, i_start + 3):
                if board[i_next][i_row] != start_owner:
                    break
                    
            else:
                height=height_count.count(board,i_start+3)
                if (i_row-height+1)==1:
                    keylanes.append(i_start+3)
                elif (i_row-height+1)==2:
                    dangerlanes.append(i_start+3)
            
        for i_start in range(1,5):
            start_owner = board[i_start][i_row]
            
            if start_owner==0:
                continue
            
            elif start_owner!=player_number:
                continue

            elif board[i_start-1][i_row]==opponent_number:
                continue
            
            for i_next in range(i_start, i_start + 3):
                if board[i_next][i_row] != start_owner:
                    break
                
            else:
                height=height_count.count(board,i_start-1)
                if (i_row-height+1)==1:
                    keylanes.append(i_start-1)
                elif (i_row-height+1)==2:
                    dangerlanes.append(i_start-1)
        
        for i_start in range(0,4):
            start_owner = board[i_start][i_row]
            ranges=[i_start,i_start+1,i_start+3]

            if start_owner==0:
                continue
            
            elif start_owner!=player_number:
                continue

            elif board[i_start+2][i_row]==opponent_number:
                continue
            
            for i_next in ranges:
                if board[i_next][i_row] != start_owner:
                    break
                
            else:
                height=height_count.count(board,i_start+2)
                if (i_row-height+1)==1:
                    keylanes.append(i_start+2)
                elif (i_row-height+1)==2:
                    dangerlanes.append(i_start+2)
                    
        for i_start in range(2,6):
            start_owner = board[i_start][i_row]
            ranges=[i_start,i_start+1,i_start-2]

            if start_owner==0:
                continue
            
            elif start_owner!=player_number:
                continue

            elif board[i_start-1][i_row]==opponent_number:
                continue
            
            for i_next in ranges:
                if board[i_next][i_row] != start_owner:
                    break
                
            else:
                height=height_count.count(board,i_start-1)
                if (i_row-height+1)==1:
                    keylanes.append(i_start-1)
                elif (i_row-height+1)==2:
                    dangerlanes.append(i_start-1)
            
    return [keylanes,dangerlanes]

def blocking_horizontal(board,player_number):
    lanes=open_lane_check.check(board)
    playernos=[1,2]
    playernos.remove(player_number)
    opponent_number=playernos[0]
    
    block = check_row(board,opponent_number)[0]
    block = [x for x in block if x in lanes]
    
    danger = check_row(board,opponent_number)[1]
    
    if len(block)!=0:
        return random.choice(block)        
    else:
        return danger

def winning_horizontal(board,player_number):
    lanes=open_lane_check.check(board)
    
    win = check_row(board,player_number)[0]
    win = [x for x in win if x in lanes]

    bait = check_row(board,player_number)[1]
    
    if len(win)!=0:
        return random.choice(win)          
    else:
        return bait

def horizontal_strat(board,player_number):
    lanes=open_lane_check.check(board)
    win=winning_horizontal(board,player_number)
    block=blocking_horizontal(board,player_number)
    if type(win)==int :
        print('using win h')
        return win
    elif type(block)==int:
        print('using block h')
        return block
    else:
        danger=block
        bait=win     
        
        no_trouble=[x for x in lanes if x not in danger+bait]
        no_more_baits=[x for x in lanes if x not in danger]
        forced_lost=danger
        
        if len(no_trouble)!=0:
            return random.choice(no_trouble)
        
        elif len(no_more_baits)!=0:
            return random.choice(no_more_baits)
        
        else:
            return random.choice(forced_lost)


#%%
board=[[0,0,0,0,0,0],[2,1,0,0,0,0],[1,1,0,0,0,0],[2,1,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
check_row(board,1)
horizontal_strat(board,1)
