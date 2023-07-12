#!/usr/bin/env python

import sys
input= sys.stdin.readline

n=int(input())
board=[]

for _ in range(n):
    board.append(list(map(int,input().split())))

visit=[[0]*n for _ in range(n)]
q=[[0,0]]

dx=[1,0]
dy=[0,1]

while q:
    x,y=q[0][0],q[0][1]
    del q[0]

    if board[x][y]==-1:
        print("HaruHaru")
        exit(0)

    jump=board[x][y]

    for i in range(2):
        nx=x+dx[i]*jump
        ny=y+dy[i]*jump

        if 0<=nx<n and 0<=ny<n and visit[nx][ny]==0:
            visit[nx][ny]=1
            q.append([nx,ny])

print("Hing")
