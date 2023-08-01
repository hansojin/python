#!/usr/bin/env python

import sys
input= sys.stdin.readline

n,m=map(int,input().split())
nums=sorted(list(map(int,input().split())))
visit = [False]*n
tmp=[]

def dfs(depth):
    if len(tmp)==m:
        print(*tmp)
        return
    rem=0
    for i in range(depth+1,n):
        if not visit[i] and nums[i]!=rem:
            tmp.append(nums[i])
            visit[i]=True
            rem=nums[i]
            dfs(i)
            tmp.pop()
            visit[i]=False

dfs(-1)

