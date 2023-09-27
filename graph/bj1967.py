#!/usr/bin/env python

import sys
input= sys.stdin.readline
sys.setrecursionlimit(100000)

n=int(input())
graph=[[] for _ in range(n+1)]

for _ in range(n-1):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))


dis = [-1]*(n+1)
dis[1]=0

def dfs(x,w):
    for i in graph[x]:
        a,b=i
        if dis[a]==-1:
            dis[a]=w+b
            dfs(a,w+b)


dfs(1,0)
far = dis.index(max(dis))
dis=[-1]*(n+1)
dis[far]=0
dfs(far,0)
print(max(dis))
