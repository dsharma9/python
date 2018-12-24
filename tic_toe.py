#!/usr/bin/env python3.7

print("This program is for Tic Toe game")

board = {'top-l':'', 'top-m':'', 'top-r':'', 'mid-l':'','mid-m':'', 'mid-r':'', 'low-l':'', 'low-m':'', 'low-r':''}

def ticToe(board):
    print(board['top-l']+ " | " + board['top-m'] + " | " + board['top-r']  )
    print("________")
    print(board['mid-l'] + " | " + board['mid-m'] + " | " + board['mid-r'] )
    print("________")
    print(board['low-l'] + " | " + board['low-m'] + " | " + board['low-r'])


turn = 'X'
for i in range(9):
    ticToe(board)
    print("The next move " + turn + " has to play")
    move=input()
    board[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'



