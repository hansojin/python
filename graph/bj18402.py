#!/usr/bin/env python

import sys
input= sys.stdin.readline
INF = sys.maxsize

from heapq import heappush
from heapq import heappop

n=int(input())
end=int(input())
timer=int(input())
m=int(input())
graph= [[] for _ in range(n+1)]
dis = [INF]*(n+1)

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
def dij(x):
    q=[]
    heappush(q,(0,x))
    dis[x]=0

    while q:
        d,now = heappop(q)
        if dis[now]<d:
            continue

        for v,w in graph[now]:
            cost = d+ w
            if cost<dis[v]:
                dis[v]=cost
                heappush(q,(cost,v))
ans=0
for i in range(1,n+1):
    dij(i)
    if dis[end]<=timer:
        ans+=1
    dis=[INF]*(n+1)
print(ans)

