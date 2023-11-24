#!/usr/bin/env python

import sys
input= sys.stdin.readline
sys.setrecursionlimit(100000000)
import math

def dfs(i):
    global cnt
    visit[i]=1
    nxt=li[i]
    if visit[nxt]==0:
        cnt+=1
        dfs(nxt)
    return cnt


n=int(input())
li=[0]+list(map(int,input().split()))
visit= [0]*(n+1)
ans=[]
    
for i in range(1,n+1):
    if not visit[i]:
        cnt=1
        dfs(i)
        ans.append(cnt)

lcm = math.lcm(*ans)
print(lcm)
