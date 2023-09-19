#!/usr/bin/env python

import sys
input= sys.stdin.readline

n=int(input())
li=[list(map(int,input().split())) for _ in range(n)]
minn=1e9

def dfs(s,nxt,v,visited):
    global minn

    if len(visited)==n:
        if li[nxt][s]!=0:
            minn=min(minn,v+li[nxt][s])
        return
    for i in range(n):
        if li[nxt][i]!=0 and i not in visited and v<minn:
            visited.append(i)
            dfs(s,i,v+li[nxt][i],visited)
            visited.pop()
for i in range(n):
    dfs(i,i,0,[i])
print(minn)
