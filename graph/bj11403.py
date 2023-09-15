#!/usr/bin/env python

import sys
input= sys.stdin.readline

INF = 1e9
n=int(input())
graph = [[INF]*n for _ in range(n)]

li=[list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if li[i][j]==1:
            graph[i][j]=1

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

for i in range(n):
    for j in range(n):
        if graph[i][j]!=INF:
            graph[i][j]=1
        else:
            graph[i][j]=0
        print(graph[i][j], end=' ')
    print()
        
