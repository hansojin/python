#!/usr/bin/env python

import sys
input= sys.stdin.readline
from collections import deque
sys.setrecursionlimit(int(1e9))

n,m=map(int,input().split())
cnt=0
li=[]
for _ in range(n):
    li.append(list(input()))
x,y=0,0
for i in range(n):
    for j in range(m):
        if li[i][j]=='I':
            x,y=i,j
            break

dx=[-1,1,0,0]
dy=[0,0,-1,1]
q=deque()
visit=[[False]*m for _ in range(n)]

def dfs(x,y):
    global cnt
    q.append((x,y))
    visit[x][y]=True

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0>nx or 0>ny or nx>=n or ny>=m or visit[nx][ny]:
            continue
        if li[nx][ny]=='X':
            continue
        if li[nx][ny]=='P':
            cnt+=1
        visit[nx][ny]=True
        dfs(nx,ny)



dfs(x,y)
if cnt==0:
    print("TT")
else:
    print(cnt)
