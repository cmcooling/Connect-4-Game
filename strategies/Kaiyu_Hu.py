# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 20:27:43 2021

@author: Kaiyu Hu
"""
def dumb(board, player_number): 
    '''
    This is a dumb strategy that only consider vertical victory. 
    It scans the whole board to find the column that has the max munber 
    of player's discs and drop a new one. If the enemy is about to win 
    (i.e. 3 discs in a column already), this code will drop a disc 
    to stop the enemy  winning first.
    '''
    my_win=[] #the columns I have a chance to win
    em_win=[] #the columes enemy has a chance to win
    
    for i_column in range(7):
        my=0 #number of my discs in a line
        em=0 #number of enemy's discs in a line
        blank=0 #number of blank grids
        
        for i_row in range (6): #scan the colume
            if board[i_column][i_row]==player_number:
                my+=1
            elif board[i_column][i_row]==0:
                blank+=1
            else:
                my=0
        
        if blank>=4-my: # I can possibly win 
            my_win.append(my) #larger my means I am morely to win next round
        else:
            my_win.append(-1)
        
        
        for i_row in range (6):
            if board[i_column][i_row]==player_number:
                em=0
            elif board[i_column][i_row]==0:
                continue
            else:
                em+=1
                
        if blank>=4-em: # The enemy can possibly win
            em_win.append(em) #larger em means enemy is morely to win next round
        else:
            em_win.append(-1)
    
    for i_column in range(7):    
        if my_win[i_column]==3:
            return i_column
            break        
    
    for i_column in range(7):
        #stop enemy winning first 
        #find the colume enemy is about to win
        if em_win[i_column]==3: 
            return i_column
            break
        
    for i_column in range(7):    
        if my_win[i_column]==max(my_win):
            return i_column
            break