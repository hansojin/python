#!/usr/bin/env python

import sys
input= sys.stdin.readline
INF = 1e9

from heapq import heappush
from heapq import heappop

f,p,c,m = map(int,input().split())
graph=[[] for _ in range(f+1)]

for _ in range(p):
    x,y,z=map(int,input().split())
    graph[x].append((y,z))
    graph[y].append((x,z))

def dij(start):
    q=[]
    distance = [INF]*(f+1)
    heappush(q,(0,start))

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

ans=[]
for i in range(5):
    loc = int(input())
    tmp = dij(loc)
    if tmp[1]<=m:
        ans.append(i+1)
print(len(ans))
for i in ans:
    print(i)
