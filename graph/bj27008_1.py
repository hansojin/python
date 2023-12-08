#!/usr/bin/env python

import heapq

def find(F, P, C, M, paths, loc):
    graph = {i: [] for i in range(1, F + 1)}

    for path in paths:
        F1, F2, T = path
        graph[F1].append((F2, T))
        graph[F2].append((F1, T))

    gc = []

    for num, cl in enumerate(loc, start=1):
        visited = set()
        min_heap = [(0, cl)]

        while min_heap:
            tt, now = heapq.heappop(min_heap)

            if now == 1:
                if tt <= M:
                    gc.append(num)
                break

            if now not in visited:
                visited.add(now)

                for nbor, ttt in graph[now]:
                    heapq.heappush(min_heap, (tt + ttt, nbor))

    return gc

F, P, C, M = map(int, input().split())

paths = [list(map(int, input().split())) for _ in range(P)]
loc = [int(input()) for _ in range(C)]

gc = find(F, P, C, M, paths, loc)

print(len(gc))
for cow in gc:
    print(cow)

