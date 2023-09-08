#!/usr/bin/env python

import sys
input= sys.stdin.readline

n=int(input())
a,b=map(int,input().split())
m=int(input())

graph = [[] for _ in range(n+1)]
visit = [0]*(n+1)
res = []

for _ in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)


def dfs(v,N):
    N+=1
    visit[v]=1

    if v==b:
        res.append(N)

    for i in graph[v]:
        if not visit[i]:
            dfs(i,N)
dfs(a,0)

if len(res)==0:
    print(-1)
else:
    print(res[0]-1)

