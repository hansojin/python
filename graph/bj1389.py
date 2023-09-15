#!/usr/bin/env python

import sys
input= sys.stdin.readline

INF = 1e9
n,m=map(int,input().split())

graph=[[1e9]*n for _ in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a-1][b-1]=1
    graph[b-1][a-1]=1

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

ans=[]
for i in range(n):
    tmp=0
    for j in range(n):
        if i!=j:
            tmp+=graph[i][j]
    ans.append(tmp)

print(ans.index(min(ans))+1)
