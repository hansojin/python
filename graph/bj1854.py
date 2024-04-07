#!/usr/bin/env python

import sys
input= sys.stdin.readline
from heapq import heappush, heappop
INF = sys.maxsize

n,m,k=map(int,input().split())
graph=[[] for _ in range(n+1)]
dp=[[INF]*k for _ in range(n+1)]
q=[]

def dij(start):
    heappush(q,[0,start])
    dp[start][0]=0
    while q:
        w,n=heappop(q)
        for nn,weight in graph[n]:
            now=weight+w
            if now<dp[nn][k-1]:
                dp[nn][k-1]=now
                dp[nn].sort()
                heappush(q,[now,nn])

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
dij(1)

print(dp)
for i in range(1,n+1):
    if dp[i][k-1]==INF:
        print(-1)
    else:
        print(dp[i][k-1])
