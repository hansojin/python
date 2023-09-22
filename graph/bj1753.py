#!/usr/bin/env python

import sys
input= sys.stdin.readline
INF = sys.maxsize

from heapq import heappush
from heapq import heappop

n,m=map(int,input().split())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)
start=int(input())
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))


def dij(x):
    q=[]
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
dij(start)
for i in range(1,n+1):
    if distance[i]==INF:
        print("INF")
    else:
        print(distance[i])

