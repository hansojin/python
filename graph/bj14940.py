#!/usr/bin/env python

import sys
input= sys.stdin.readline
from collections import deque

n,m=map(int,input().split())
li=[]
for _ in range(n):
    li.append(list(map(int,input().split())))

zero=0
for i in range(n):
    zero+=li[i].count(0)

visit = [[False]*m for _ in range(n)]


for i in range(n):
    for j in range(m):
        if li[i][j]==2:
            x,y=i,j
            visit[x][y]=True
            li[x][y]=0
            break


dq= deque()

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(a,b):
    dq.append((a,b))
    while dq:
        x,y=dq.popleft()
        visit[x][y]=1
        for i in range(4):
            nx= x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m and not visit[nx][ny] and li[nx][ny]==1:
                li[nx][ny]=li[x][y]+1
                visit[nx][ny]=True           
                dq.append((nx,ny))
            
bfs(x,y)

ztwo=0
for i in range(n):
    ztwo+=visit[i].count(0)

if zero == ztwo:
    for i in range(n):
        for j in range(m):
            print(li[i][j],end=' ')
        print()

else:
    for i in range(n):
        for j in range(m):
            if li[i][j]==1 and visit[i][j]==False:
                print(-1, end=' ')
            else:
                print(li[i][j],end= ' ')
        print()

