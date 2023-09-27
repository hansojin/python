#!/usr/bin/env python

import sys
input =sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
li,ans = [],[]

for i in range(n):
    li.append(list(map(int, input().split())))

def bfs(a, b):
    q = deque()
    q.append((a, b))
    li[a][b] = 0
    cnt = 1

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if li[nx][ny] == 1:
                li[nx][ny] = 0
                q.append((nx, ny))
                cnt += 1
    ans.append(cnt)

for i in range(n):
    for j in range(m):
        if li[i][j] == 1:
            bfs(i, j)


if len(ans) == 0:
    print(len(ans))
    print(0)
else:
    print(len(ans))
    print(max(ans))
