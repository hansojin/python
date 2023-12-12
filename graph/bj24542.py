#!/usr/bin/env python

import sys
input= sys.stdin.readline
from collections import deque,defaultdict

def bfs(x, visit, graph):
    q = deque([x])
    visit[x] = True
    num = 1

    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if visit[nxt]:
                continue
            q.append(nxt)
            visit[nxt] = True
            num += 1

    return num


graph = defaultdict(list)
N, M = map(int, input().split())
visit = [False for _ in range(N+1)]
ans = 1
mod = 1000000007

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for v in range(1, N+1):
    if not visit[v]:
        ans *= bfs(v, visit, graph)
        ans %= mod

print(ans)
