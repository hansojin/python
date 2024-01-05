#!/usr/bin/env python

import sys
input= sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10000)

n,m,v=map(int,input().split())
graph=[[] for _ in range(n+1)]
bvisit=[0]*(n+1)
dvisit=[0]*(n+1)

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

bli,dli=[],[]
def bfs(x):
    q=deque()
    q.append(x)
    bvisit[x]=1
    bli.append(x)

    while q:
        now = q.popleft()
        for i in graph[now]:
            if not bvisit[i]:
                q.append(i)
                bli.append(i)
                bvisit[i]=1

def dfs(x):
    dli.append(x)
    dvisit[x]=1
    
    for i in graph[x]:
        if not dvisit[i]:
            dfs(i)

dfs(v)
print(*dli)
bfs(v)
print(*bli)


