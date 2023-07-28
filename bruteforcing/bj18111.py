#!/usr/bin/env python

import sys
input= sys.stdin.readline

li=[]
n,m,b=map(int,input().split())
for _ in range(n):
    li.append(list(map(int,input().split())))

height,ans=0,1e9

for i in range(257):
    max,min=0,0
    for j in range(n):
        for k in range(m):
            if li[j][k]<i:
                min+=(i-li[j][k])
            else:
                max+=li[j][k]-i
    inv=max+b
    if inv<min:
        continue
    time=2*max+min
    if time<=ans:
        ans=time
        height=i
print(ans,height)
