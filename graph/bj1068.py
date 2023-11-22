#!/usr/bin/env python

import sys
input= sys.stdin.readline

def dfs(n):
    global ans
    if graph[n]:
        for i in graph[n]:
            dfs(i)
    else:
        ans+=1
    return ans
n=int(input())
li=list(map(int,input().split()))
m=int(input())
ans=0
root = li.index(-1)
if m==root:
    print(0)
else:
    graph = [[] for _ in range(n+1)]
    for i in range(n):
        if li[i]!=-1:
            if i==m:
                continue
            graph[li[i]].append(i)

    graph[m]=[]
    print(dfs(root))
