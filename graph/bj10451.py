#!/usr/bin/env python

import sys
input= sys.stdin.readline
sys.setrecursionlimit(2000)

def dfs(i):
    visit[i]=1
    nxt=li[i]
    if visit[nxt]==0:
        dfs(nxt)
    return


for _ in range(int(input())):
    n=int(input())
    li=[0]+list(map(int,input().split()))
    visit= [0]*(n+1)
    ans=0

    for i in range(1,n+1):
        if not visit[i]:
            dfs(i)
            ans+=1
    print(ans)


