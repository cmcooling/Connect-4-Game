#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 19:47:49 2021

@author: fanchao
"""
import random

def win(board,player_num):
    zi = player_num
    for i in range(0,6):
        if board[i].count(zi) > 2:
            return [1,i]
        else:
            return [0,0]

def lose(board,player_num):
    zi = player_num
    if player_num == 2:
        zi = 1
    for i in range(0,6):
        if board[i].count(zi) > 2:
            return [1,i]  
        else:
            return [0,0]

def smart(board,player_num):
    if win(board,player_num)[0] == 1:
        a=win(board,player_num)[1]
    elif lose(board,player_num)[0] == 1:
        a=lose(board,player_num)[1]
    else:
        a=random.randint(0,6)
    if board[a].count(0)==0:       
        board.remove(a)
        return a+1
    else: 
        return a