#!/usr/bin/env python

import sys
input= sys.stdin.readline
from collections import deque

n=int(input())
li=[list(input().strip()) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if li[i][j]=="F":
            x,y=i,j
            break

dx=[1,1,1,-1,-1,-1,0]
dy=[-1,0,1,-1,0,1,-1]

def bfs(x,y,cnt):
    q=deque()
    q.append((x,y,cnt))
    while q:
        x,y,cnt=q.popleft()
        for i in range(7):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if li[nx][ny]=="#":
                continue
            if li[nx][ny]=='.':
                li[nx][ny]='0'
                q.append((nx,ny,cnt+1))
    return cnt


print(bfs(x,y,0))
