#!/usr/bin/env python

import sys
input= sys.stdin.readline
import heapq
INF = int(1e9)

n,m,k,x = map(int,input().split())
graph = [[] for i in range(n+1)]
dist = [INF]*(n+1)

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append((b,1))

def dij(x):
    q=[]
    heapq.heappush(q,(0,x))
    dist[x]=0

    while q:
        distance, now = heapq.heappop(q)
        if dist[now]<distance:
            continue
        for i in graph[now]:
            cost = distance+i[1]
            if cost<dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
dij(x)

if dist.count(k)==0:
    print(-1)
else:
    for i in range(1,n+1):
        if dist[i]==k:
            print(i)

