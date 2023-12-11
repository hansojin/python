#!/usr/bin/env python

import sys
input= sys.stdin.readline

n,m=map(int,input().split())
li=[]
for _ in range(n):
    li.append(list(map(int,input().split())))

bf,up=0,0
for i in range(n):
    for j in range(m):
        if j==0:
            bf=0
        else:
            bf=li[i][j-1]
        if i==0:
            up=0
        else:
            up=li[i-1][j]
        li[i][j]=max(li[i][j]+bf, li[i][j]+up)
print(li[-1][-1])
