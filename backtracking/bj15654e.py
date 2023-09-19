#!/usr/bin/env python

n,m=map(int,input().split())
li=sorted(list(map(int,input().split())))

arr=[]
visit = [False]*n

def dfs(cnt):
    if len(arr)==m:
        print(*arr)
        return
    for i in range(n):
        if visit[i]:
            continue
        visit[i]=True
        arr.append(li[i])
        dfs(cnt+1)
        arr.pop()
        visit[i]=False
dfs(0)
