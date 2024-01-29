#!/usr/bin/env python

import sys
input= sys.stdin.readline
from collections import deque

n=int(input())
indegree = [0]*(n+1)
graph=[[] for i in range(n+1)]
dp=[0]*(n+1)
t=[0]

for i  in range(1,n+1):
    li=list(map(int,input().split()))
    t.append(li[0])
    if li[1]!=0:
        for j in range(2,len(li)):
            graph[li[j]].append(i)
            indegree[i]+=1

q=deque()
for i in range(1,n+1):
    if indegree[i]==0:
        q.append(i)
        dp[i]=t[i]
while q:
    now=q.popleft()
    for i in graph[now]:
        indegree[i]-=1
        dp[i]=max(dp[now]+t[i],dp[i])
        if indegree[i]==0:
            q.append(i)
print(max(dp))
