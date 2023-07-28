#!/usr/bin/env python
#bipartite matching

import sys
input= sys.stdin.readline

n,m=map(int,input().split())
cow = [ [] for _ in range(n)]
visit = [-1] * m
cnt =0

for i in range(n):
    tmp = list(map(int,input().split()))
    for j in tmp[1:]:
        j-=1;
        cow[i].append(j)

def dfs(x):
    for i in cow[x]:
        if check[i]:
            continue
        check[i]=True
        if visit[i]==-1 or dfs(visit[i]):
            visit[i]=x
            return True
    return False



for i in range(n):
    check=[False]*m
    if dfs(i):
        cnt+=1

print(cnt)
