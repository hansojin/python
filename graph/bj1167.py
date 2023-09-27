#!/usr/bin/env python

import sys
input= sys.stdin.readline
sys.setrecursionlimit(100000)

n=int(input())
graph=[[] for _ in range(n+1)]

for _ in range(n):
    nums=list(map(int,input().split()))
    a=nums.index(-1)
    for i in range(1,a,2):
        graph[nums[0]].append((nums[i],nums[i+1]))
        graph[nums[i]].append((nums[0],nums[i+1]))

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

