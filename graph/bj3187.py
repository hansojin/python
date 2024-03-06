#!/usr/bin/env python

import sys
input= sys.stdin.readline
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    q.append((x,y))
    c[x][y]=1
    vcnt,kcnt=0,0
    while q:
        x,y=q.popleft()
        if a[x][y]=='v':
            vcnt+=1
        elif a[x][y]=='k':
            kcnt+=1
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<m and 0<=ny<n:
                if a[nx][ny]!='#' and not c[nx][ny]:
                    c[nx][ny]=1
                    q.append((nx,ny))
    if vcnt>=kcnt:
        kcnt=0
    else:
        vcnt=0
    return [vcnt,kcnt]

m, n = map(int, input().split())
a = [list(input().strip()) for _ in range(m)]
c = [[0]*n for _ in range(m)]
q = deque()

v, k = 0, 0
for i in range(m):
    for j in range(n):
        if a[i][j] != '#' and not c[i][j]:
            vcnt, kcnt = bfs(i, j)
            v += vcnt; k += kcnt
print(k, v)
