#!/usr/bin/env python

import sys
input= sys.stdin.readline
from collections import deque
sys.setrecursionlimit(100000)

n,m=map(int,input().split())
li=[[] for _ in range(n)]
visit = [False]*n
flag= False

for _ in range(m):
    a,b=map(int,input().split())
    li[a].append(b)
    li[b].append(a)

def dfs(n,depth):
    global flag
    visit[n]=True
    if depth==5:
        flag=True
        return
    for i in li[n]:
        if visit[i]==False:
            dfs(i,depth+1)
    visit[n]=False

for i in range(n):
    dfs(i,1)
    if flag:
        break

if flag:
    print(1)
else:
    print(0)
    
