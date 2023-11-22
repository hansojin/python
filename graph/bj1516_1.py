#!/usr/bin/env python

import sys
input= sys.stdin.readline
from collections import deque

n=int(input())
graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1)
cost = [0]*(n+1)

for i in range(1,n+1):
    data=list(map(int,input().split()))[:-1]
    cost[i]=data[0]
    tmp=data[1:]

    for t in tmp:
        graph[t].append(i)
        indegree[i]+=1

def topology_sort():
    res=[0]*(n+1)
    q=deque()

    for i in range(1,n+1):
        if indegree[i]==0:
            q.append(i)
    while q:
        now = q.popleft()
        res[now]+=cost[now]

        for i in graph[now]:
            indegree[i]-=1
            res[i]=max(res[i],res[now])
            if indegree[i]==0:
                q.append(i)
    for i in range(1,n+1):
        print(res[i])

topology_sort()

