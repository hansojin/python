#!/usr/bin/env python

import sys
input= sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m=map(int,input().split())
li=[list(map(int,input().split())) for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]
visit=[[0]*m for _ in range(n)]
cnt,sizes=0,[]

def dfs(x,y,s):
    visit[x][y]=1
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]

        if 0<=nx<n and 0<=ny<m:
            if li[nx][ny] and not visit[nx][ny]:
                s=dfs(nx,ny,s+1)
    return s

for i in range(n):
    for j in range(m):
        if li[i][j] and not visit[i][j]:
            cnt+=1
            sizes.append(dfs(i,j,1))

print(cnt)
if sizes:
    print(max(sizes))
else:
    print(0)

