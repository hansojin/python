#!/usr/bin/env python

import sys
input= sys.stdin.readline
from collections import deque

n,m=map(int,input().split())
li=[list(input()) for _ in range(m)]
visit=[[0]*n for _ in range(m)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y,c):
    cnt=1
    q=deque()
    q.append((x,y))
    visit[x][y]=1

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<m and 0<=ny<n:
                if li[nx][ny]==c and not visit[nx][ny]:
                    visit[nx][ny]=1
                    q.append((nx,ny))
                    cnt+=1
    return cnt

w,b=0,0
for i in range(m):
    for j in range(n):
        if li[i][j]=='W' and not visit[i][j]:
            w+=bfs(i,j,'W')**2
        elif li[i][j]=='B' and not visit[i][j]:
            b+=bfs(i,j,'B')**2
print(w,b)


