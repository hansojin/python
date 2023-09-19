#!/usr/bin/env python

n=int(input())
arr=[]

def dfs(cnt):
    if len(arr)==n:
        print(*arr)
        return
    for i in range(n):
        if (i+1) not in arr:
            arr.append(i+1)
            dfs(cnt+1)
            arr.pop()
dfs(0)
