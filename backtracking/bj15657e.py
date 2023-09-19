#!/usr/bin/env python

n,m=map(int,input().split())
li=sorted(list(map(int,input().split())))

arr=[]

def dfs(cnt):
    if len(arr)==m:
        print(*arr)
        return
    for i in range(cnt,n):
        arr.append(li[i])
        dfs(i)
        arr.pop()
dfs(0)

