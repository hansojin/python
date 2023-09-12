#!/usr/bin/env python

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
li = {}
visit = set()

dx = [-2, 2, 0, 0]
dy = [0, 0, -2, 2]

for _ in range(k):
    a, b = map(int, input().split())
    x, y = a - 1, b - 1
    li[(x, y)] = 10

for x, y in li.keys():
    for i in range(4):
        nx = x+ dx[i]
        ny = y + dy[i]
        if 0>nx or nx>=n or 0>ny or ny>=n:
            continue
        if (nx,ny) in li and li[(nx, ny)] == 10:
            continue
        
        visit.add((nx,ny))

print(len(visit))

