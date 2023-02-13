#!/usr/bin/env python

n,m=map(int,input().split())

visit = [False for _ in range(n)]
arr = []

def dfs(cnt):
    if cnt==m:
        print(*arr)
        return
    for i in range(n):
        if not visit[i]:
            visit[i]=True
            arr.append(i+1)
            dfs(cnt+1)
            visit[i]=False
            arr.pop()
dfs(0)
