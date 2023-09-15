#!/usr/bin/env python

import sys
input= sys.stdin.readline

INF = 1e9
n=int(input())
graph= [[INF]*n for _ in range(n)]

for i in range(n):
    graph[i][i]=0

while True:
    a,b=map(int,input().split())
    if a==b==-1:
        break
    graph[a-1][b-1]=1
    graph[b-1][a-1]=1
    
for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j]==1 or graph[i][j]==0:
                continue
            elif graph[i][j]> graph[i][k]+graph[k][j]:
                graph[i][j]= graph[i][k]+graph[k][j]

r=[]
for i in range(n):
    r.append(max(graph[i]))
m=min(r)
print(m,r.count(m))
for i,v in enumerate(r):
    if v==m:
        print(i+1,end=' ')

