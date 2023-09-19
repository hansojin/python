#!/usr/bin/env python

n,m=map(int,input().split())
li=sorted(list(map(int,input().split())))

arr=[]

def dfs(d):
    if d==m:
        print(' '.join(map(str,arr)))
        return
    visit=0
    for i in range(n):
        if visit!=li[i]:
            arr.append(li[i])
            visit=li[i]
            dfs(d+1)
            arr.pop()
dfs(0)
