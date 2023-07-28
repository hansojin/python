#!/usr/bin/env python

import sys
input= sys.stdin.readline
sys.setrecursionlimit(100000)

n,m=map(int,input().split())
work= [[] for _ in range(n)]
done = [-1]*n
cnt=0

for i in range(m):
    a,b=map(int,input().split())
    a-=1
    b-=1
    work[a].append(b)

def dfs(x):
    for i in work[x]:
        if check[i]:
            continue
        check[i]=True
        if done[i]==-1 or dfs(done[i]):
            done[i]=x
            return True
    return False


for i in range(n):
    check=[False]*n
    if dfs(i):
        cnt+=1
print(cnt)

