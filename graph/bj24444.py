#!/usr/bin/env python

import sys
input = sys.stdin.readline
from collections import deque

n,m,r = map(int,input().split())
graph= [[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n):
    graph[i].sort()

visit=[0]*(n+1)
cnt=1


def bfs(srt):
    global cnt
    
    q=deque([r])
    visit[srt]=1
    
    while q:
        srt=q.popleft()
        for adj_node in graph[srt]:
            if visit[adj_node]==0:
                cnt+=1
                visit[adj_node]=cnt
                q.append(adj_node)

bfs(r)

for i in visit[1:]:
    print(i)
