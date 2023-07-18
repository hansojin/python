#!/usr/bin/env python

import sys
input= sys.stdin.readline

board=[]
for _ in range(5):
    board.append(list(map(int,input().split())))

call =[]
for _ in range(5):
    call+=list(map(int,input().split()))

def check():
    bingo=0

    for x in board:
        if x.count(0)==5:
            bingo+=1

    for i in range(5):
        y=0
        for j in range(5):
            if board[j][i]==0:
                y+=1
        if y==5:
            bingo+=1

    d1=0
    for i in range(5):
        if board[i][i]==0:
            d1+=1
    if d1==5:
        bingo+=1
    
    d2=0
    for i in range(5):
        if board[i][4-i]==0:
            d2+=1
    if d2==5:
        bingo+=1

    return bingo

cnt=0
for k in range(25):
    for i in range(5):
        for j in range(5):
            if call[k]==board[i][j]:
                board[i][j]=0
                cnt+=1

    if cnt>=12:
        result = check()
        if result>=3:
            print(k+1)
            break

