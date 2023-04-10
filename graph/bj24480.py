#!/usr/bin/env python

import sys
input =sys.stdin.readline
sys.setrecursionlimit(10**9)

n,m,r=map(int,input().split())

graph=[[] for _ in range(n+1)]
visit=[0]*(n+1)
ans=[0]*(n+1)
count=1

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(srt):
    global count
    ans[srt]=count
    visit[srt]=1

    graph[srt].sort(reverse=True)

    for adj_node in graph[srt]:
        if visit[adj_node]==0:
            count+=1
            dfs(adj_node)

dfs(r)

for i in ans[1:]:
    print(i)
