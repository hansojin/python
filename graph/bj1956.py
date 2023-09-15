#!/usr/bin/env python

import sys
input= sys.stdin.readline

INF = 1e9
v,e=map(int,input().split())
g=[[INF]*v for _ in range(v)]

for _ in range(e):
    a,b,c=map(int,input().split())
    g[a-1][b-1]=c

for k in range(v):
    for i in range(v):
        for j in range(v):
            g[i][j]=min(g[i][j], g[i][k]+g[k][j])
ans=INF
for i in range(v):
    for j in range(v):
        ans=min(ans,g[i][i])
if ans==INF:
    ans=-1
print(ans)


