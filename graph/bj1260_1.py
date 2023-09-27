#!/usr/bin/env python

import sys
input= sys.stdin.readline
from collections import deque

n,m,v = map(int,input().split())
graph=[[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1

v1 = [0]*(n+1)
v2 = [0]*(n+1)

def dfs(v):
    v1[v] = 1
    print(v, end=' ')
    for i in range(1,n+1):
        if not v1[i] and graph[v][i]:
            dfs(i)

def bfs(v):
    q=deque([v])
    v2[v]=1
    while q:
        v=q.popleft()
        print(v,end=' ')
        for i in range(1,n+1):
            if not v2[i] and graph[v][i]:
                q.append(i)
                v2[i]=1
dfs(v)
print()
bfs(v)
