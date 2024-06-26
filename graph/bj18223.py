#!/usr/bin/env python

import sys
input= sys.stdin.readline
INF= sys.maxsize

from heapq import heappush
from heapq import heappop

V,E,P = map(int,input().split())
graph = [[]for _ in range(V+1)]
distance = [INF for _ in range(V+1)]
for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

def dijkstra(start):
    heap = []
    heappush(heap,[0,start])
    distance = [INF for _ in range(V + 1)]
    distance[start] = 0
    while heap:
        cost, curr = heappop(heap)
        for next,c in graph[curr]:
            totalCost = cost + c
            if distance[next] > totalCost:
                distance[next] = totalCost
                heappush(heap,[totalCost,next])
    return distance

if dijkstra(1)[V] == dijkstra(1)[P] + dijkstra(P)[V]:
    print("SAVE HIM")
else:
    print("GOOD BYE")
