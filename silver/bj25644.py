#!/usr/bin/env python

import sys
input= sys.stdin.readline

INF = int(1e9)
n=int(input())
li=list(map(int,input().split()))
minn=li[0]
res=0

for i in range(1,n):
    if minn<li[i]:
        res=max(res,li[i]-minn)
    else:
        minn=li[i]
print(res)
