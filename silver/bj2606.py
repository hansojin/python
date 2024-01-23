#!/usr/bin/env python

import sys
input= sys.stdin.readline

n=int(input())
m=int(input())

graph=[[] for _ in range(n+1)]
visit=[0]*(n+1)

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt=0
def dfs(n):
    global cnt
    visit[n]=1

    for i in graph[n]:
        if not visit[i]:
            visit[i]=1
            cnt+=1
            dfs(i)
dfs(1)
print(cnt)

