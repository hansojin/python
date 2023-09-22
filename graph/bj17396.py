#!/usr/bin/env python

import sys
input= sys.stdin.readline
INF = sys.maxsize

from heapq import heappush
from heapq import heappop

n,m=map(int,input().split())
graph= [[] for _ in range(n+1)]
dist = [INF] * (n+1)

li=list(map(int,input().split()))
li[-1]=0
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dij(x):
    q=[]
    heappush(q,(0,x))
    dist[x]=0

    while q:
        d,now = heappop(q)
        if dist[now]<d:
            continue

        for v,w in graph[now]:
            cost = d + w
            if cost<dist[v] and li[v]==0:
                dist[v]=cost
                heappush(q,(cost,v))
dij(0)
if dist[n-1]==INF:
    print(-1)
else:
    print(dist[n-1])


