#!/usr/bin/env python

import sys
input= sys.stdin.readline
from collections import deque

n,m=map(int,input().split())
li=[list(map(int,input().split())) for _ in range(n)]

dx=[0,0,-1,1]
dy=[-1,1,0,0]

def bfs():
    q=deque()
    q.append((0,0))
    visit[0][0]=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and visit[nx][ny]==0:
                if li[nx][ny]>=1:
                    li[nx][ny]+=1
                else:
                    visit[nx][ny]=1
                    q.append((nx,ny))
cnt=0
while True:
    visit=[[0]*m for _ in range(n)]
    bfs()
    flag=0
    for i in range(n):
        for j in range(m):
            if li[i][j]>=3:
                li[i][j]=0
                flag=1
            elif li[i][j]==2:
                li[i][j]=1
    if flag:
        cnt+=1
    else:
        break
print(cnt)

