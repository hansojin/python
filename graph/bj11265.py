#!/usr/bin/env python

import sys
input= sys.stdin.readline

n,m=map(int,input().split())
graph=[ list(map(int,input().split())) for _ in range(n)]

for k in range(n):
    for a in range(n):
        for b in range(n):
            if graph[a][b] > graph[a][k] + graph[k][b]:
                graph[a][b] = graph[a][k] + graph[k][b]

for _ in range(m):
    a,b,c = map(int,input().split())
    print("Enjoy other party" if graph[a-1][b-1] <=c else "Stay here")
