#!/usr/bin/env python

import sys
input= sys.stdin.readline
from collections import deque

n=int(input())
li=[]
for _ in range(n):
    li.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if li[i][j]<n:
            li[i][j]=0
        else:
            li[i][j]=1
dx=[-1,1,0,0]
dy=[0,0,-1,1]

visit = [[0]*n for _ in range(n)]

dq = deque()
def bfs(a,b):
    dq.append((a,b))
    visit[a][b]=1
    while dq:
        x,y=dq.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<n and visit[nx][ny]==0:
                visit[nx][ny]=1
                dq.append((nx,ny))
                li[nx][ny]=0

bfs(0,0)

cnt=0
for i in li:
    cnt+=i.count(1)
print(cnt)
