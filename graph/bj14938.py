#!/usr/bin/env python

import sys
input= sys.stdin.readline

n,m,r=map(int,input().split())
item = list(map(int,input().split()))

INF = 1e9
g = [[INF]*n for _ in range(n)]

for _ in range(r):
    a,b,c=map(int,input().split())
    g[a-1][b-1]=min(g[a-1][b-1], c)
    g[b-1][a-1]=min(g[b-1][a-1], c)

for i in range(n):
    g[i][i]=0

for k in range(n):
    for a in range(n):
        for b in range(n):
            g[a][b]=min(g[a][b],g[a][k]+g[k][b])
ans=0
for i in range(n):
    tmp=0
    for j in range(n):
        if g[i][j]<=m:
            tmp+=item[j]
    ans=max(ans,tmp)
print(ans)

