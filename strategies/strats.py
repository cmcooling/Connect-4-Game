import random



def ckboardme(board, player_number, column):
    for row in range(4,0,-1):
        if board[column][row] == player_number and board[column][row+1] == 0:
                return True
    else:
        return False
        
def ckboardmt0(board, player_number, column):
    if board[column][0] == 0:
        return True
    else:
        return False
def ckboardmt1(board, player_number, column):
    if board[column][1] == 0:
        return True
    else:
        return False
def ckboardmt2(board, player_number, column):
    if board[column][2] == 0:
        return True
    else:
        return False    
def ckboardmt3(board, player_number, column):
    if board[column][3] == 0:
        return True
    else:
        return False            
def ckboardmt4(board, player_number, column):
    if board[column][4] == 0:
        return True
    else:
        return False
def ckboardmt5(board, player_number, column):
    if board[column][5] == 0:
        return True
    else:
        return False
    
def ckputv3(board, player_number, column):
    for row in range(0, 2):
        if board[column][row] == player_number and board[column][row+1] == player_number and  board[column][row+2] == player_number and (board[column][row+3] == 0): 
            return True 
        
def ckputhl3(board, player_number, column):
     for row in range(6):
        if board[column][row] == 0 and board[column+1][row] == player_number and  board[column+2][row] == player_number and board[column+3][row] == player_number: 
            return True 
def ckputhr3(board, player_number, column):
     for row in range(6):
        if board[column][row] == 0 and board[column-1][row] == player_number and  board[column-2][row] == player_number and board[column-3][row] == player_number: 
            return True 

def ckputhl21(board, player_number, column):
     for row in range(6):
        if board[column][row] == 0 and board[column-1][row] == player_number and  board[column+1][row] == player_number and board[column+2][row] == player_number: 
            return True 
def ckputhr21(board, player_number, column):
     for row in range(6):
        if board[column][row] == 0 and board[column+1][row] == player_number and  board[column-1][row] == player_number and board[column-2][row] == player_number: 
            return True         
        
        
        
        
        
        
        
        
     
def ckblockv3(board, opponent_number, column):
    for row in range(2):
        if board[column][row] == opponent_number and board[column][row+1] == opponent_number and  board[column][row+2] == opponent_number and board[column][row+3] == 0: 
            return True 
def ckblockhl3(board, opponent_number, column):
     for row in range(6):
        if board[column][row] == 0 and board[column+1][row] == opponent_number and  board[column+2][row] == opponent_number and board[column+3][row] == opponent_number: 
            return True 
def ckblockhr3(board, opponent_number, column):
     for row in range(6):
        if board[column][row] == 0 and board[column-1][row] == opponent_number and  board[column-2][row] == opponent_number and board[column-3][row] == opponent_number: 
            return True   
def ckblockhl21(board, opponent_number, column):
     for row in range(6):
        if board[column][row] == 0 and board[column-1][row] == opponent_number and  board[column+1][row] == opponent_number and board[column+2][row] == opponent_number: 
            return True 
def ckblockhr21(board, opponent_number, column):
     for row in range(6):
        if board[column][row] == 0 and board[column+1][row] == opponent_number and  board[column-1][row] == opponent_number and board[column-2][row] == opponent_number: 
            return True              
        
def ckinvalid(board, column):
    if board[column][5]!= 0:
        return False
    else:
        return True
def ckrowfill(board, row):
    for column in range(7):
        if board[column][row]== 0:
                return True
    else:
        return False
    
    
    

def strat(board, player_number):
    opponent_number = 0
    if player_number == 1:
        opponent_number = 2
    if player_number == 2:
        opponent_number = 1
    
    if board[3][0] == 0:
            return(3)
    if board[3][0] == opponent_number and board[3][1] == 0:
            return(3)
        
    for column in range(7):
        if ckputv3(board, player_number, column) and ckinvalid(board, column) == True:
            return (column)
    for column in range(4):
        if ckputhl3(board, player_number, column) == True:
            return column
    for column in range(6, 3, -1):
        if ckputhr3(board, player_number, column) == True:
            return column  
    for column in range(1, 4):
        if ckputhl21(board, player_number, column) == True:
            return column
    for column in range(5, 2, -1):
        if ckputhr21(board, player_number, column) == True:
            return column    
        
        
        
        
    for column in range(7):
        if ckblockv3(board, opponent_number, column) and ckinvalid(board, column) == True:
            return (column)      
    for column in range(4):
        if ckblockhl3(board, opponent_number, column) == True:
            return column
    for column in range(6, 3, -1):
        if ckblockhr3(board, opponent_number, column) == True:
            return column   
    for column in range(1, 4):
        if ckblockhl21(board, opponent_number, column) == True:
            return column
    for column in range(5, 2, -1):
        if ckblockhr21(board, opponent_number, column) == True:
            return column    
    
    #for column in range(6):
     #   if ckboardme(board, player_number, column) and ckinvalid(board, column) == True:
      #      return (column) 
    
    
    for column in range(7):
        if ckboardmt0(board, player_number, column) == True:
            return (column)
    for column in range(7):   
        if ckboardmt1(board, player_number, column) == True:
            return (column)
    for column in range(7):    
        if ckboardmt2(board, player_number, column) == True:
            return (column)
    for column in range(7):    
        if ckboardmt3(board, player_number, column) == True:
            return (column)
    for column in range(7):    
        if ckboardmt4(board, player_number, column) == True:
            return (column)
    for column in range(7):
        if ckboardmt5(board, player_number, column) == True:
            return (column)
        
    valid_columns = []
    for columns in range(7):
        if board[columns][5] == 0:
            valid_columns.append(columns)
    return(random.choice(valid_columns))
       
   
    

        
        
        