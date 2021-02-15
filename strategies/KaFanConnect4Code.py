# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 21:52:00 2021

@author: Hayes
"""

def Kf2(board, player_number):
    '''Ka Fan Methodical Function'''
    for i_column in range(6, -1, -1):
        if min(board[i_column])==1:
            return i_column
        if max(board[3]) ==0:
            return 3
        if max(board[2]) ==0:
            return 2
        if max(board[4]) ==0:
            return 4
        if max(board[1]) ==0:
            return 1
        if max(board[5]) ==0:
            return 5
        if max(board[0]) ==0:
            return 0
        if max(board[6]) ==0:
            return 6
    for i_column in range(7):        
        if max(board[i_column]) != 0:
            return i_column
        if min(board[i_column])==0:
            return i_column