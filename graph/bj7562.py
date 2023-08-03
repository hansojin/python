#!/usr/bin/env python

from collections import deque
import sys
input= sys.stdin.readline

t = int(input().rstrip())


def bfs() :
    dx = [-1, 1, 2, 2, 1, -1, -2, -2]
    dy = [2, 2, 1, -1, -2, -2, -1, 1]

    q = deque()
    q.append((hx, hy))
    while q :
        x, y = q.popleft()
        if x == ex and y == ey :
            return matrix[x][y] -1 
        for i in range(8) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<l and 0<=ny<l and matrix[nx][ny] == 0 :
                matrix[nx][ny] = matrix[x][y] + 1
                q.append((nx,ny))
                
            
        
for _ in range(t) :
    l = int(input().rstrip())
    hx, hy = map(int, input().rstrip().split())
    ex, ey = map(int, input().rstrip().split())
    matrix = [[0]*l for _ in range(l)]
    matrix[hx][hy] = 1
    print(bfs())

