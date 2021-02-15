#%%
import random
#from New_strats import vertical_strats
from New_strats import vertical_strats as vs, horizontal_strats as hs, diagonal_strats as ds, open_lane_check

def Strat(board,player_number):
    lanes=open_lane_check.check(board)
    winV=vs.winning_vertical(board,player_number)
    winH=hs.winning_horizontal(board,player_number)
    winD=ds.winning_diagonal(board,player_number)
    
    blockV=vs.blocking_vertical(board,player_number)
    blockH=hs.blocking_horizontal(board,player_number)
    blockD=ds.blocking_diagonal(board,player_number)
    
    if type(winV)==int :
        print('using win V')
        return winV
    elif type(winH)==int :
        print('using win H')
        return winH
    elif type(winD)==int :
        print('using win D')
        return winD
    
    elif type(blockV)==int:
        print('using block V')
        return blockV
    elif type(blockH)==int:
        print('using block H')
        return blockH
    elif type(blockD)==int:
        print('using block D')
        return blockD
    
    else:
        danger=blockV+blockH+blockD
        print("danger=",danger)
        bait=winV+winH+winD
        print("bait=",bait)
        
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
board=[[1,2,2,2,1,2],[1,2,1,2,2,2],[1,2,2,2,1,2],[1,2,1,2,1,2],[1,2,1,2,1,2],[1,1,1,2,0,0],[1,2,2,2,1,0]]
#winning_vertical(board,1)
vs.vertical_strat(board,1)