#!/usr/bin/env python

import sys
input= sys.stdin.readline
INF = sys.maxsize

from heapq import heappush
from heapq import heappop

n=int(input())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(int(input())):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

start,end= map(int,input().split())

def dij(x):
    q=[]
    heappush(q,(0,x))
    distance[x]=0

    while q:
        dist,now = heappop(q)
        if distance[now]<dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heappush(q,(cost,i[0]))
dij(start)
print(distance[end])
