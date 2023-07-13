#!/usr/bin/env python

from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(li,a,b):
    q=deque()
    q.append((a,b))
    li[a][b]=0

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0>nx or nx>=n or ny<0 or ny>=m:
                continue
            if li[nx][ny]==1:
                li[nx][ny]=0
                q.append((nx,ny))
    return

for _ in range(int(input())):
    n,m,k=map(int,input().split())
    li=[[0 for _ in range(m)] for _ in range(n)]

    for i in range(k):
        x,y=map(int,input().split())
        li[x][y]=1

    cnt=0
    for a in range(n):
        for b in range(m):
            if li[a][b]==1:
                bfs(li,a,b)
                cnt+=1
    print(cnt)

