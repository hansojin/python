#!/usr/bin/env python

import sys
input= sys.stdin.readline
INF = int(1e9)

n,m,p = map(int,input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    graph[i][i]=0

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a][b]=c
    graph[b][a]=c

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][b]> graph[a][k] + graph[k][b]:
                graph[a][b] =  graph[a][k] + graph[k][b]

for _ in range(p):
    a,b=map(int,input().split())
    print(graph[a][b])
