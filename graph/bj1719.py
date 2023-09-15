#!/usr/bin/env python

import sys
input= sys.stdin.readline

n,m=map(int,input().split())
INF = 1e9
graph = [[INF]*n for _ in range(n)]
ans= [[0]*n for _ in range(n)]

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a-1][b-1]=c
    graph[b-1][a-1]=c
    ans[a-1][b-1]=b-1
    ans[b-1][a-1]=a-1

for i in range(n):
    graph[i][i]=0
    ans[i][i]=INF

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] >graph[i][k]+graph[k][j]: 
                graph[i][j] =graph[i][k]+graph[k][j]
                ans[i][j]=ans[i][k]


for i in range(n):
    for j in range(n):
        if ans[i][j]== INF:
            print('-', end=' ')
        else:
            print(ans[i][j]+1,end =' ')
    print()

