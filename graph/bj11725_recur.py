#!/usr/bin/env python

import sys
input= sys.stdin.readline
sys.setrecursionlimit(1000000)

n=int(input())
visit=[0]*(n+1)
ans=[0]*(n+1)
e=[[] for _ in range(n+1)]

for i in range(n-1):
    a,b=map(int,input().split())
    e[a].append(b)
    e[b].append(a)

def dfs(e,v,visit):
    visit[v]=1
    for i in e[v]:
        if not visit[i]:
            ans[i]=v
            dfs(e,i,visit)

dfs(e,1,visit)
for i in range(2,n+1):
    print(ans[i])

