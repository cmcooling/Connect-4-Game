
  
def from_middle(board,player_number):
    for i_column in range(0,7):
        for i_row in range(0,6):
            if board[i_column][i_row] in [1,2] and min(board[i_column])==0:
                if board[i_column][i_row] == board[i_column][i_row - 1] and board[i_column][i_row - 2]:
                    if board[i_column][i_row+1]==0:
                        return(i_column)
                elif min(board[i_column])==0:
                    if i_column in [1,2,3,4]:
                        if board[i_column+1][i_row] in [1,2] and board[i_column+1][i_row]== board[i_column-1][i_row] or board[i_column+2][i_row]:
                            if board[i_column][i_row-1] !=0 and board[i_column][i_row]==0:
                                return(i_column)
                    elif i_column in [2,3,4,5]:
                        if board[i_column-1][i_row] in [1,2] and board[i_column-1][i_row]== board[i_column-2][i_row] or board[i_column+1][i_row]:
                            if board[i_column][i_row-1] !=0 and board[i_column][i_row]==0:
                                return(i_column)
    if min(board[3])==0:
        return(3)
    elif min(board[4])==0:
        return(4)
    elif min(board[2])==0:
        return(2)
    elif min(board[5])==0:
        return(5)
    elif min(board[1])==0:
        return(1)
    elif min(board[6])==0:
        return(6)
    else:
        return(0)

            

   
            
        
        

    
        

        
             
        
    
    

    

