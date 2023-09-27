#!/usr/bin/env python

import sys
input= sys.stdin.readline
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(a, b):
    sheep = 0
    wolf = 0

    q = deque()
    q.append((a, b))

    if li[a][b] == 'o':
        sheep += 1
    elif li[a][b] == 'v':
        wolf += 1

    li[a][b] = '#'

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if  0 <= nx < r and 0 <= ny < c and li[nx][ny] != "#":
                if li[nx][ny] == 'o':
                    sheep += 1
                elif li[nx][ny] == 'v':
                    wolf += 1

                li[nx][ny] = '#'
                q.append((nx, ny))

    if wolf >= sheep:
        return 0, wolf
    elif sheep > wolf:
        return sheep, 0




r, c = map(int, input().split())
li = []

ts,tw=0,0

for i in range(r):
    li.append(list(input()))

for i in range(r):
    for j in range(c):
        if li[i][j] in 'ov':
            tmps, tmpw = bfs(i, j)
            ts += tmps
            tw += tmpw

print(ts, tw)
