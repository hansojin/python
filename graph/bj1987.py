#!/usr/bin/env python

import sys
input= sys.stdin.readline

n,m=map(int,input().split())
li=[]
for _ in range(n):
    li.append(list(input()))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

ans=0
s=set()

def dfs(x,y,cnt):
    global ans
    ans=max(cnt,ans)
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m and not li[nx][ny] in s:
            s.add(li[nx][ny])
            dfs(nx,ny,cnt+1)
            s.remove(li[nx][ny])
s.add(li[0][0])
dfs(0,0,1)
print(ans)
