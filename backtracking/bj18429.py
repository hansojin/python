#!/usr/bin/env python

import sys
input= sys.stdin.readline

n,k=map(int,input().split())
li=list(map(int,input().split()))
check = [False]*n

cnt=0
def dfs(d,t):
    global cnt
    if d==n:
        cnt+=1
        return
    for i in range(n):
        if check[i] or t+li[i]-k<0:
            continue
        check[i]=True
        dfs(d+1, t+li[i]-k)
        check[i]=False

dfs(0,0)
print(cnt)
