#!/usr/bin/env python

import sys
input= sys.stdin.readline

w,h,x,y,p=map(int,input().split())
cnt=0

for _ in range(p):
    X,Y=map(int,input().split())

    if (x<=X<=x+w) and (y<=Y<=y+h):
        cnt+=1
        continue

    r=h/2
    d1=((X-x)**2 + (Y-(y+r))**2)**0.5
    d2=((X-(x+w))**2 + (Y-(y+r))**2)**0.5
    if d1<=r or d2<=r:
        cnt+=1
print(cnt)
