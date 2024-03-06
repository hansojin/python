#!/usr/bin/env python

import sys
input= sys.stdin.readline
from collections import deque

n,m=map(int,input().split())
li=[]
for _ in range(n):
    li.append(list(map(int,input().split())))

cnt=0
dx=[-1,1,0,0,-1,-1,1,1]
dy=[0,0,-1,1,-1,1,-1,1]

def bfs(li,a,b):
    q=deque()
    q.append((a,b))
    li[a][b]=0

    while q:
        x,y=q.popleft()
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if li[nx][ny]==1:
                    li[nx][ny]=0
                    q.append((nx,ny))
    return

for a in range(n):
    for b in range(m):
        if li[a][b]==1:
            bfs(li,a,b)
            cnt+=1
print(cnt)
