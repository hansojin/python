#!/usr/bin/env python

import sys
input= sys.stdin.readline

n,sc,p=map(int,input().split())
if n==0:
    print(1)
else:
    li=list(map(int,input().split()))
    if n==p and li[-1]>=sc:
        print(-1)
    else:
        res=n+1
        for i in range(n):
            if li[i]<=sc:
                res=i+1
                break
        print(res)
