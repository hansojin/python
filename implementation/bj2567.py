#!/usr/bin/env python

import sys
input= sys.stdin.readline

sx,sy=101,101
bx,by=0,0

li=[[0]*103 for _ in range(103)]

for _ in range(int(input())):
    x,y=map(int,input().split())
    for i in range(y,y+10):
        for j in range(x,x+10):
            li[i][j]=1
    if sx>x:
        sx=x
    if sy>y:
        sy=y
    if bx<x+10:
        bx=x+10
    if by<y+10:
        by=y+10
ans=0
for i in range(sy-1,by+2):
    for j in range(sx-1,bx+2):
        if li[i][j]^li[i+1][j]:
            ans+=1
        if li[i][j]^li[i][j+1]:
            ans+=1
print(ans)
    
