#!/usr/bin/env python

import sys
input= sys.stdin.readline

n,m=map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))

tmp=[[0]*(m+1) for _ in range(n+1)]
for mm in range(1,n+1):
    for nn in range(1,m+1):
        tmp[mm][nn]=tmp[mm][nn-1]+tmp[mm-1][nn] - tmp[mm-1][nn-1] + arr[mm-1][nn-1]

k=int(input())
for i in range(k):
    i,j,x,y=map(int,input().split())
    print(tmp[x][y]-tmp[i-1][y]-tmp[x][j-1]+tmp[i-1][j-1])

