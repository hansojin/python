#!/usr/bin/env python

import sys
input= sys.stdin.readline
INF = int(1e9)

from heapq import heappush
from heapq import heappop

n,m = map(int,input().split())
graph=[[] for _ in range(n+1)]

for _ in range(m):
    x,y,z=map(int,input().split())
    graph[x].append((y,z))
    graph[y].append((x,z))

a,b = map(int,input().split())

def dij(x):
    q=[]
    heappush(q,(0,x))
    distance = [INF]*(n+1)
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

ori = dij(1)
aa,bb =dij(a),dij(b)

one = ori[a] + aa[b]+ bb[n]
two = ori[b] + bb[a] + aa[n]
res = min(one,two)
print(res if res<INF else -1)
