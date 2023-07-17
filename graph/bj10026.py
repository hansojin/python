#!/usr/bin/env python

import sys
sys.setrecursionlimit(1000000)
input= sys.stdin.readline

n = int(input().rstrip())
graph = [list(input().rstrip()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

cnt1, cnt2 = 0, 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    visited[x][y] = 1
    now = graph[x][y]

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if (0 <= nx < n) and (0 <= ny < n):
            if visited[nx][ny]==0:
                if graph[nx][ny] == now:
                    dfs(nx,ny)

for i in range(n):
    for j in range(n):
        if visited[i][j]==0:
            dfs(i,j)
            cnt1 += 1

for i in range(n):
    for j in range(n):
        if graph[i][j]=='R':
            graph[i][j]='G'

visited = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i,j)
            cnt2 += 1

print(cnt1,cnt2)
