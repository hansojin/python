#!/usr/bin/env python

import sys
input= sys.stdin.readline
from collections import deque

n,m=map(int,input().split())
arr=[]
shark=deque()

for i in range(n):
    tmp=list(map(int,input().split()))
    for j in range(m):
        if tmp[j]==1:
            shark.append((i,j))
    arr.append(tmp)

dx=[-1, -1, -1, 0, 1, 0, 1, 1]
dy=[-1, 0, 1, 1, 1, -1, 0, -1]

def bfs():
    while shark:
        x,y=shark.popleft()
        for i in range(8):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if arr[nx][ny]==0:
                    shark.append((nx,ny))
                    arr[nx][ny]=arr[x][y]+1
    return

bfs()
maxx=0
for i in range(n):
    for j in range(m):
        maxx=max(maxx,arr[i][j])
print(maxx-1)
