#!/usr/bin/env python

import sys
input= sys.stdin.readline
from collections import deque

n,m,k=map(int,input().split())
li= [[0]*(m) for _ in range(n)]
for _ in range(k):
    a,b=map(int,input().split())
    li[a-1][b-1]=1

q=deque()
dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans=[]
def bfs(a,b):
    q.append((a,b))
    li[a][b]=0
    cnt=1

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if li[nx][ny]==1:
                cnt+=1
                q.append((nx,ny))
                li[nx][ny]=0
    ans.append(cnt)

for i in range(n):
    for j in range(m):
        if li[i][j]==1:
            bfs(i,j)
print(max(ans))
