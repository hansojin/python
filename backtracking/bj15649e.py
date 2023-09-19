#!/usr/bin/env python

n,m=map(int,input().split())

arr=[]
check = [False]*n

def dfs(cnt):
    if cnt==m:
        print(*arr)
        return
    for i in range(n):
        if check[i]:
            continue
        check[i]=True
        arr.append(i+1)
        dfs(cnt+1)
        arr.pop()
        check[i]=False
dfs(0)
