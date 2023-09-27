#!/usr/bin/env python

import sys
input= sys.stdin.readline
sys.setrecursionlimit(1000000)

n,m,r = map(int,input().split())
graph = [[] for _ in range(n+1)]
visit = [-1]*(n+1)

for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

def dfs(v,d):
    visit[v]=d

    for i in graph[v]:
        if visit[i]==-1:
            dfs(i,d+1)
    return

dfs(r,0)

for i in range(1,n+1):
    print(visit[i])

