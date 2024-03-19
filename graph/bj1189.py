#!/usr/bin/env python

import sys
input= sys.stdin.readline

r,c,K=map(int,input().split())
graph=[list(input().rstrip()) for _ in range(r)]
ans=0

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y,k):
    global ans
    if x==0 and y==(c-1) and k==K:
        ans+=1
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<r and 0<=ny<c and graph[nx][ny]!='T':
            graph[nx][ny]='T'
            dfs(nx,ny,k+1)
            graph[nx][ny]='.'
graph[r-1][0]='T'
dfs(r-1,0,1)
print(ans)
