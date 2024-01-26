#!/usr/bin/env python

import sys
input= sys.stdin.readline
INF=100001

for _ in range(int(input())):
    n,m=map(int,input().split())
    dist=[[INF]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        a,b,c=map(int,input().split())
        dist[a][b]=c
        dist[b][a]=c

    k=int(input())
    room=list(map(int,input().split()))

    for k in range(1,n+1):
        dist[k][k]=0
        for i in range(1,n+1):
            for j in range(1,n+1):
                dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])

    dmin=float(INF)
    nmin=0

    for i in range(1,n+1):
        hap=sum(dist[r][i] for r in room)
        if dmin>hap:
            dmin=hap
            nmin=i
    print(nmin)

