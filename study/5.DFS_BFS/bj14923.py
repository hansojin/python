#!/usr/bin/env python 

from collections import deque

n, m=map(int, input().split())
hy, hx=map(int, input().split())
ey, ex=map(int, input().split())
hy, hx, ey, ex=hy-1, hx-1, ey-1, ex-1
graph=[list(map(int, input().split())) for _ in range(n)]
dy, dx=[0, 1, 0, -1], [1, 0, -1, 0]
def bfs(y, x):
    q=deque()
    q.append((y, x, 0, 1))
    visit=[[[False for _ in range(2)] for _ in range(m)] for _ in range(n)]
    visit[y][x][1]=True
    while q:
        y, x, cnt, magic=q.popleft()
        if (y, x)==(ey, ex):
            return cnt
        for i in range(4):
            ny, nx=y+dy[i], x+dx[i]
            if 0<=ny<n and 0<=nx<m:
                if visit[ny][nx][magic]:
                    continue
                if graph[ny][nx]==1 and magic==1:
                    visit[ny][nx][0]=True
                    q.append((ny, nx, cnt+1, magic-1))
                elif graph[ny][nx]==0:
                    visit[ny][nx][magic]=True
                    q.append((ny, nx, cnt+1, magic))
    return -1
print(bfs(hy, hx))
