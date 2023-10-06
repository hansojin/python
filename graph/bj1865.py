#!/usr/bin/env python

import sys
input= sys.stdin.readline
INF = 1e9

def bf(start):
    dist[start] = 0
    for i in range(1, n+1):
        for s in range(1, n+1):
            for next, time in graph[s]:
                if dist[next] > dist[s] + time:
                    dist[next] = dist[s] + time
                    if i == n: 
                        return True
    return False

TC = int(input())
for i in range(TC):
    n, m, w = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    dist = [INF for _ in range(n+1)]
    for j in range(m):
        s, e, t = map(int, input().split())
        graph[s].append([e, t])
        graph[e].append([s, t])
    for k in range(w):
        s, e, t = map(int, input().split())
        graph[s].append([e, -t])

    neg_cycle = bf(1)
    if not neg_cycle:
        print('NO')
    else:
        print('YES')
