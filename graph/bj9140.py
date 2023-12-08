#!/usr/bin/env python

import sys
input= sys.stdin.readline
import heapq
INF = int(1e9)

while True:
    n,s,st,nd = map(int,input().split())
    if n==s==st==nd==0:
        break
    graph = [[] for i in range(n+1)]
    dist = [INF]*(n+1)

    for _ in range(s):
        a,b,c=map(int,input().split())
        graph[a].append((b,c))

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
    dij(st)
    print(dist[nd])

