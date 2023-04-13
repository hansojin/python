#!/usr/bin/env python

import sys
input = sys.stdin.readline

n=int(input())
graph=[[] for _ in range(n+1)]

for _ in range(int(input())):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt=0
visit= [0]*(n+1)

def dfs(n):
    global cnt
    visit[n]=1

    for adj_node in graph[n]:
        if visit[adj_node]==0:
            cnt+=1
            visit[adj_node]=1
            dfs(adj_node)

dfs(1)
print(cnt)
