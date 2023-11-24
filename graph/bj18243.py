#!/usr/bin/env python

import sys
input= sys.stdin.readline
INF = int(1e9)

n,m=map(int,input().split())
graph = [[INF] *n for _ in range(n)]

for i in range(n):
    graph[i][i]=0

for _ in range(m):
    a,b=map(int,input().split())
    graph[a-1][b-1]=1
    graph[b-1][a-1]=1

for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


maxx=0
for i in graph:
    maxx=max(max(i),maxx)
if maxx>6:
    print('Big World!')
else:
    print('Small World!')

