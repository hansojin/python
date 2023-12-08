#!/usr/bin/env python

import sys
input= sys.stdin.readline
import heapq
INF = sys.maxsize

n,s,e = map(int,input().split())
graph = [[] for i in range(n+1)]
dist = [INF]*(n+1)

for _ in range(n):
    tmp=list(map(int,input().split()))
    for i in range(len(tmp)-1):
        graph[tmp[0]].append((tmp[i+1],1))

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
dij(s)
if dist[e] ==INF:
    print(-1)
else:
    print(dist[e]-1)
