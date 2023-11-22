#!/usr/bin/env python

import sys
input= sys.stdin.readline
from collections import deque

n,m=map(int,input().split())
graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1)

for i in range(m):
    li=list(map(int,input().split()))
    for i in range(1,li[0]):
        graph[li[i]].append(li[i+1])
        indegree[li[i+1]]+=1

def topology_sort():
    res=[]
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
    if len(res)==n:
        for i in res:
            print(i)
    else:
        print(0)


topology_sort()

