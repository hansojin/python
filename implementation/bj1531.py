#!/usr/bin/env python

import sys
input= sys.stdin.readline

n,m=map(int,input().split())
lx,ly=100,100
rx,ry=0,0
li=[[0]*101 for _ in range(101)]
for _ in range(n):
    a,b,c,d=map(int,input().split())
    if lx>a:
        lx=a
    if ly>b:
        ly=b
    if rx<c:
        rx=c
    if ry<d:
        ry=d
    for x in range(a,c+1):
        for y in range(b,d+1):
            li[x][y]+=1

cnt=0
for i in range(lx,rx+1):
    for j in range(ly,ry+1):
        if li[i][j]>m:
            cnt+=1
    
print(cnt)
