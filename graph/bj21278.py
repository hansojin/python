#!/usr/bin/env python

import sys
input= sys.stdin.readline
INF = int(1e9)

n,m=map(int,input().split())

graph=[[INF]*(n+1) for _ in range(n+1)]


for i in range (1, n+1):
    graph[i][i]=0

for _ in range(m):
    a,b= map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b]= min(graph[a][b], graph[a][k] + graph[k][b])

minn=INF
res=[]
for a in range(1, n):
    for b in range(2, n+1):
        summ=0
        for k in range(1,n+1):
            summ+=min(graph[k][a],graph[k][b])*2
        if summ<minn:
            minn=summ
            res=[a,b,summ]
print(*res)
