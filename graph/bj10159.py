#!/usr/bin/env python

import sys
input= sys.stdin.readline

n=int(input())
m=int(input())

graph=[[0]*(n+1) for _ in range(n+1)]
for i in range(n+1):
    graph[i][i]=0

for _ in range(m):
    a,b=map(int,input().split())
    graph[a][b]=1
    
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if graph[i][k] and graph[k][j]:
                graph[i][j]=1

for a in range(1,n+1):
    cnt=0
    for b in range(1,n+1):
        if not graph[a][b] and not graph[b][a]:
            cnt+=1
    print(cnt-1)



