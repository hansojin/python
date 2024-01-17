#!/usr/bin/env python

import sys
input= sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n=int(input())
li = []

for _ in range(n):
    row = input().rstrip()
    li.append(row)

dist = [[-1] *(n+1) for _ in range(n+1)]
dist[0][0]=0

q = deque()
q.append((0,0))


while q:
    p = q.popleft()
    x, y = p[0], p[1]

    for k in range(4):
        nx = dx[k] + x
        ny = dy[k] + y
        if (0 <= nx < n and 0 <= ny < n):
            if dist[nx][ny]!=-1:
                continue

            if li[nx][ny] == '1':
                q.append((nx,ny))
                dist[nx][ny] = dist[x][y] + 1
            else:
                q.appendleft((nx,ny))
                dist[nx][ny] = dist[x][y]

print(dist[1][1])

