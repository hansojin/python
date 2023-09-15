#!/usr/bin/env python

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
front = [[] for _ in range(n+1)]
back = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int ,input().split())
    front[a].append(b)
    back[b].append(a)

def bfs(start, front):
    visited = [False] * (n+1)
    queue = deque([start])
    visited[start] = True
    cnt = 0

    while queue:
        now = queue.popleft()
        cnt += 1
        for next in front[now]:
            if not visited[next]:
                queue.append(next)
                visited[next] = True

    return cnt

ans = 0
for i in range(1, n+1):
    if bfs(i, front) + bfs(i, back) - 1 == n:
        ans += 1

print(ans)
