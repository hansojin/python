#!/usr/bin/env python

import sys
input= sys.stdin.readline
INF = sys.maxsize
from heapq import heappush, heappop

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
distance=[-1]*(n+1)

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dij(start):
    q=[]
    heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now=heappop(q)
        for i in graph[now]:
            if distance[i]==-1:
                distance[i]=dist+1
                heappush(q,(distance[i],i))

dij(1)
print(distance.index(max(distance)),max(distance),distance.count(max(distance)))
