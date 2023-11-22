#!/usr/bin/env python

import sys
input= sys.stdin.readline
from collections import deque

n,m=map(int,input().split())
graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1)
res=[1]*(n+1)
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    indegree[b]+=1

def topology_sort():
    q=deque()

    for i in range(1,n+1):
        if indegree[i]==0:
            q.append(i)
    while q:
        now = q.popleft()
        res.append(now)

        for i in graph[now]:
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)
                res[i]=res[now]+1

topology_sort()
for i in range(1,n+1):
    print(res[i],end= ' ')


