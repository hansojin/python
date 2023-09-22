#!/usr/bin/env python

import sys
input= sys.stdin.readline
INF = sys.maxsize

from heapq import heappush
from heapq import heappop

n,m,end=map(int,input().split())
graph = [[] for i in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))


def dij(x):
    q=[]
    distance = [INF] * (n+1)
    heappush(q,(0,x))
    distance[x]=0

    while q:
        dist,now = heappop(q)
        if distance[now]<dist:
            continue

        for v,w in graph[now]:
            cost = dist + w
            if cost<distance[v]:
                distance[v]=cost
                heappush(q,(cost,v))
    return distance

back = dij(end)
back[0]=0
for i in range(1,n+1):
    go =dij(i)
    back[i]+=go[end]
print(max(back))

