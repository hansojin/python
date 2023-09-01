#!/usr/bin/env python


from collections import deque

n, m = map(int, input().split())

dx = [1, 2, 2, 1]
dy = [2, 1, -1, -2]

def bfs(x, y):
    visited = [[0] * m for _ in range(n)]
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < m and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

    return visited[n-1][m-1]

print(bfs(0, 0))

