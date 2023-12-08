#!/usr/bin/env python

import sys
input= sys.stdin.readline
from heapq import heappush, heappop

def dij():
    q=[]
    heappush(q,(cave[0][0],0,0))
    dist[0][0]=0

    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    while q:
        cost,x,y=heappop(q)
        if x==y==n-1:
            print(f'Problem {cnt}: {dist[x][y]}')
            break
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>(n-1) or ny>(n-1):
                continue
            ncost = cost+cave[nx][ny]
            if ncost<dist[nx][ny]:
                dist[nx][ny]=ncost
                heappush(q,(ncost,nx,ny))

cnt=1
while True:
    n=int(input())
    if n==0:
        break
    cave=[list(map(int,input().split())) for _ in range(n)]
    dist=[[1e9]*n for _ in range(n)]

    dij()
    cnt+=1
