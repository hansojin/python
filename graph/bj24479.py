#!/usr/bin/env python

import sys
input =sys.stdin.readline

n,m,r = map(int,input().split())

graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)  #as undirected graph

for i in range(1,len(graph)):
    graph[i].sort(reverse=True)
    # to pop in asc -> arrange in desc

def dfs(srt):
    
    stack=[srt]
    visit=[0]*(n+1)
    idx=[0]*(n+1)
    cnt=1

    while stack:
        node=stack.pop()

        if visit[node]==1:
            continue
        
        visit[node]=1
        idx[node]=cnt
        cnt+=1

        for adj_node in graph[node]:    
            #지금 해당 노드의 인접 노드들을 다 stack에 넣어주기
            if visit[adj_node]==0:
                stack.append(adj_node)

    return idx

idx=dfs(r)
print(*idx[1:],sep='\n')
