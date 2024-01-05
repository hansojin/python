#!/usr/bin/env python

import sys
input= sys.stdin.readline
import heapq
INF = int(1e9)

n=int(input())
m=int(input())
graph=[[] for i in range(n+1)]
dist=[INF]*(n+1)

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

def dij(x):
    q=[]
    heapq.heappush(q,(0,x))
    dist[x]=0

    while q:
        w,cur = heapq.heappop(q)
        if dist[cur]<w:
            continue
        for g in graph[cur]:
            cost = w+g[1]
            if cost<dist[g[0]]:
                dist[g[0]]=cost
                heapq.heappush(q,(cost,g[0]))
dij(1)

cnt=-1
for i in dist:
    if i<=2:
        cnt+=1
print(cnt)

