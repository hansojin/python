#!/usr/bin/env python

import sys
input= sys.stdin.readline
from bisect import bisect_left

for _ in range(int(input())):
    n,m=map(int,input().split())
    aLi=sorted(list(map(int,input().split())))
    bLi=sorted(list(map(int,input().split())))

    cnt=0
    for a in aLi:
        cnt+=(bisect_left(bLi,a))
    print(cnt)

